from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    print("🦬 BuffaloOS is starting...")
    print("   Hoima Buffalo Hotel & Business Hub")
    print("   Open your browser at: http://localhost:5000")
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)