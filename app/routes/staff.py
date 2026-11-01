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
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: #0f3460;
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: #16213e;
            border: 2px solid #00b4d8;
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            max-width: 400px;
            width: 90%;
        }
        .emoji { font-size: 60px; margin-bottom: 16px; }
        h1 { color: #00b4d8; margin-bottom: 8px; }
        p { color: #aaa; margin: 6px 0; }
        .badge {
            background: #00b4d8;
            color: #16213e;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">👷</div>
        <h1>Staff Dashboard</h1>
        <p>Buffalo Hotel Operations Centre</p>
        <p>Requests appear here in real time</p>
        <div class="badge">Ready for requests ✅</div>
    </div>
</body>
</html>
""")