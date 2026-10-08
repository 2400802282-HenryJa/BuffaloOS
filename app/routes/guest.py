from flask import Blueprint, render_template_string
from app.models import Room

guest_bp = Blueprint('guest', __name__, url_prefix='/guest')

@guest_bp.route('/<int:room_id>')
def guest_home(room_id):
    # Temporary — no database lookup yet, just confirm routing works
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BuffaloOS - Room {{ room_id }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #1a1a2e;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: #16213e;
                border: 2px solid #f5a623;
                border-radius: 16px;
                padding: 40px;
                text-align: center;
                max-width: 400px;
            }
            .emoji { font-size: 60px; margin-bottom: 16px; }
            h1 { color: #f5a623; margin: 0 0 8px 0; }
            p { color: #aaa; }
            .badge {
                background: #f5a623;
                color: #1a1a2e;
                padding: 6px 16px;
                border-radius: 20px;
                font-weight: bold;
                display: inline-block;
                margin-top: 16px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="emoji">🦬</div>
            <h1>Hoima Buffalo Hotel</h1>
            <p>Welcome, Room {{ room_id }} Guest</p>
            <p>Your digital concierge is loading...</p>
            <div class="badge">BuffaloOS is ALIVE</div>
        </div>
    </body>
    </html>
    """, room_id=room_id)
