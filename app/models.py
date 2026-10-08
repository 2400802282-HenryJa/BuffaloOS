from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    role = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='available')
    floor = db.Column(db.Integer)
    price_ugx = db.Column(db.Float, nullable=False)
    has_ac = db.Column(db.Boolean, default=True)
    has_wifi = db.Column(db.Boolean, default=True)
    max_guests = db.Column(db.Integer, default=2)
    notes = db.Column(db.Text)
    service_requests = db.relationship('ServiceRequest', backref='room', lazy=True)

class HousekeepingLog(db.Model):
    __tablename__ = 'housekeeping_logs'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    action = db.Column(db.String(50))
    notes = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')

class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    guest_name = db.Column(db.String(100))
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), default='normal')
    status = db.Column(db.String(20), default='pending')
    assigned_to = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    resolution_note = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'room_id': self.room_id,
            'guest_name': self.guest_name,
            'category': self.category,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'submitted_at': self.submitted_at.strftime('%Y-%m-%d %H:%M'),
        }

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    content = db.Column(db.Text, nullable=False)
    notif_type = db.Column(db.String(30))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reference_id = db.Column(db.Integer)
