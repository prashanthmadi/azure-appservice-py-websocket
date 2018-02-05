import os
from waitress import serve
from main import socketio,app
socketio.run(app,host="0.0.0.0",port=int(os.environ["PORT"].rstrip()))
