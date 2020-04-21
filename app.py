import base64
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from urllib.request import urlretrieve
from mimetypes import guess_extension
app = Flask(__name__)
socketio = SocketIO(app, always_connect=True, engineio_logger=True)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/image', methods=["PUT"])
def imageRoute():
    image_url=request.headers['URL']
    image_url_strip = image_url[image_url.find("/9"):]
    decodedimage=base64.b64decode(image_url_strip)
    print(decodedimage)
    new_image_handle = open('new_test_image.jpg', 'wb')
    new_image_handle.write(decodedimage)
    new_image_handle.close()
    return "Good", 200


if __name__ == '__main__':
    app.run()
