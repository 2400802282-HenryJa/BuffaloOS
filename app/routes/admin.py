from flask import Blueprint, render_template_string

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_dashboard():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>BuffaloOS - Owner Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: #1b0000;
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: #2d0000;
            border: 2px solid #ff4444;
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            max-width: 400px;
            width: 90%;
        }
        .emoji { font-size: 60px; margin-bottom: 16px; }
        h1 { color: #ff4444; margin-bottom: 8px; }
        p { color: #aaa; margin: 6px 0; }
        .badge {
            background: #ff4444;
            color: white;
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
        <div class="emoji">📊</div>
        <h1>Owner Dashboard</h1>
        <p>Hoima Buffalo Hotel — Full Overview</p>
        <p>All systems operational</p>
        <div class="badge">BuffaloOS Admin ✅</div>
    </div>
</body>
</html>
""")