from flask import Blueprint, render_template, request, jsonify, abort
from app import socketio
from app.models import db, Room, ServiceRequest

guest_bp = Blueprint('guest', __name__, url_prefix='/guest')

# Allowed categories (must match the buttons on the page) and their default priority
CATEGORY_PRIORITY = {
    'Plumbing': 'high',
    'Electrical': 'high',
    'AC & Heating': 'high',
    'Security': 'urgent',
    'Cleaning': 'normal',
    'TV & Entertainment': 'normal',
    'Room Service': 'normal',
    'Bedding & Towels': 'normal',
    'Other': 'normal',
}


@guest_bp.route('/<int:room_id>')
def guest_home(room_id):
    room = Room.query.filter_by(room_number=str(room_id)).first()
    if not room:
        abort(404)
    return render_template('guest/portal.html', room_id=room_id)


@guest_bp.route('/<int:room_id>/submit', methods=['POST'])
def submit_request(room_id):
    room = Room.query.filter_by(room_number=str(room_id)).first()
    if not room:
        return jsonify({'success': False, 'error': 'Unknown room.'}), 404

    data = request.get_json(silent=True) or {}
    category = (data.get('category') or '').strip()
    description = (data.get('description') or '').strip()[:500]
    guest_name = (data.get('guest_name') or '').strip()[:80] or f'Room {room_id} Guest'

    if category not in CATEGORY_PRIORITY:
        return jsonify({'success': False, 'error': 'Please choose a category.'}), 400
    if len(description) < 5:
        return jsonify({'success': False, 'error': 'Please add a little more detail.'}), 400

    new_request = ServiceRequest(
        room_id=room.id,
        guest_name=guest_name,
        category=category,
        description=description,
        priority=CATEGORY_PRIORITY[category],
        status='pending',
    )

    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'success': False, 'error': 'Could not save your request. Please try again.'}), 500

    # Tell the staff dashboard immediately
    socketio.emit('new_request', new_request.to_dict(), to='staff')

    return jsonify({
        'success': True,
        'request_id': new_request.id,
        'message': 'Your request has been received.'
    })