import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = Flask(__name__)
app = socketio.WSGIApp(sio, app)

speed_limit = 10


def img_preprocess(img):
    try:
        # Crop, YUV, blur, resize, normalize
        img = img[60:135, :, :]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.resize(img, (200, 66))  # (width, height)
        img = img / 255.0
        return img
    except Exception as e:
        print('Preprocessing error:', e)
        return np.zeros((66, 200, 3), dtype=np.float32)

@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    throttle = 1.0 - speed/speed_limit
    print('{} {} {}'.format(steering_angle, throttle, speed))
    send_control(steering_angle, throttle)

@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0.0, 0.0)

def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })

if __name__ == '__main__':
    print("Loading model...")
    model = load_model('model/model.h5', compile=False)
    print("Model loaded.")
    app = socketio.WSGIApp(sio, app)
    print("Starting server...")
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
