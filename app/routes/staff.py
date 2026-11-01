from datetime import datetime
from flask import Blueprint, render_template, jsonify, request
from flask_socketio import join_room
from app import socketio
from app.models import db, ServiceRequest

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

PRIORITY_ORDER = {'urgent': 0, 'high': 1, 'normal': 2, 'low': 3}

# Which status changes are allowed from each current status
VALID_NEXT = {
    'pending': {'in_progress', 'resolved'},
    'assigned': {'in_progress', 'resolved'},
    'in_progress': {'resolved'},
}


@socketio.on('join_staff')
def on_join_staff():
    # No login yet. Phase 3 (authentication) will protect this.
    join_room('staff')


@staff_bp.route('/')
def staff_dashboard():
    return render_template('staff/dashboard.html')


@staff_bp.route('/api/requests')
def list_requests():
    open_items = ServiceRequest.query.filter(
        ServiceRequest.status.in_(['pending', 'assigned', 'in_progress'])
    ).all()
    open_items.sort(key=lambda r: (PRIORITY_ORDER.get(r.priority, 2), r.submitted_at))

    recent = (ServiceRequest.query.filter_by(status='resolved')
              .order_by(ServiceRequest.resolved_at.desc()).limit(10).all())

    return jsonify({
        'open': [r.to_dict() for r in open_items],
        'resolved': [r.to_dict() for r in recent],
    })


@staff_bp.route('/api/requests/<int:req_id>/status', methods=['POST'])
def update_status(req_id):
    data = request.get_json(silent=True) or {}
    new_status = data.get('status')
    note = (data.get('note') or '').strip()[:300]

    req = db.session.get(ServiceRequest, req_id)
    if not req:
        return jsonify({'success': False, 'error': 'Request not found'}), 404
    if new_status not in VALID_NEXT.get(req.status, set()):
        return jsonify({'success': False, 'error': 'That change is not allowed'}), 400

    req.status = new_status
    if new_status == 'resolved':
        req.resolved_at = datetime.utcnow()
        req.resolution_note = note or None

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'success': False, 'error': 'Could not save'}), 500

    payload = req.to_dict()
    socketio.emit('request_updated', payload, to='staff')
    return jsonify({'success': True, 'request': payload})