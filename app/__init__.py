from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import db

socketio = SocketIO()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    
    with app.app_context():
        db.create_all()
        print(" ✅ Database tables created")
        
    from app.routes.auth import auth_bp
    from app.routes.guest import guest_bp
    from app.routes.staff import staff_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(admin_bp)
    
    return app
