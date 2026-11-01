from flask import Blueprint, render_template_string

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head><title>BuffaloOS - Login</title></head>
<body style="background:#111;color:white;display:flex;
justify-content:center;align-items:center;height:100vh;
font-family:Arial;">
    <h2>🦬 BuffaloOS Login — Coming Soon</h2>
</body>
</html>
""")