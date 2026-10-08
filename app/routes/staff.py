from flask import Blueprint, render_template_string

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/')
def staff_dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>BuffaloOS - Staff</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f3460;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .card {
                background: #16213e;
                border: 2px solid #00b4d8;
                border-radius: 16px;
                padding: 40px;
                text-align: center;
            }
            h1 { color: #00b4d8; }
            .badge {
                background: #00b4d8;
                color: #16213e;
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
            <div style="font-size:60px">👷</div>
            <h1>Staff Dashboard</h1>
            <p>Buffalo Hotel Operations Centre</p>
            <div class="badge">Ready for requests</div>
        </div>
    </body>
    </html>
    """)
