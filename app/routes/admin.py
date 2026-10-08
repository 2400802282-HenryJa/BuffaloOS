from flask import Blueprint, render_template_string

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BuffaloOS - Admin</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #1b0000;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: #2d0000;
                border: 2px solid #ff4444;
                border-radius: 16px;
                padding: 40px;
                text-align: center;
            }
            h1 { color: #ff4444; }
            .badge {
                background: #ff4444;
                color: white;
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
            <div style="font-size:60px">📊</div>
            <h1>Owner Dashboard</h1>
            <p>Hoima Buffalo Hotel — Full Overview</p>
            <div class="badge">All systems operational</div>
        </div>
    </body>
    </html>
    """)
