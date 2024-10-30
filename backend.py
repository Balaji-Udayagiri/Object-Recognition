from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io
import time
import base64

app = Flask(__name__)
socketio = SocketIO(app)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Check if an image file was uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    # Read and process the image
    file = request.files['image']
    image = Image.open(file)
    image = np.array(image)

    # Run YOLO model on the image
    results = model(image)
    if len(results[0].boxes) > 0:
        annotated_image = results[0].plot()  # Draw bounding boxes if objects are detected
    else:
        annotated_image = image  # Return the original image if nothing is detected

    # Convert the processed image to JPEG for download
    _, buffer = cv2.imencode('.jpg', annotated_image)
    img_base64 = base64.b64encode(buffer).decode('utf-8')

    return jsonify({'processed_image': f'data:image/jpeg;base64,{img_base64}'})

@socketio.on('video_frame')
def handle_video_frame(data):
    # Decode base64 image from frontend
    img_data = base64.b64decode(data.split(",")[1])
    np_arr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # Run YOLO model on the frame
    results = model(frame)
    annotated_frame = results[0].plot()  # Draw bounding boxes

    # Encode annotated frame back to base64
    _, buffer = cv2.imencode('.jpg', annotated_frame)
    frame_b64 = base64.b64encode(buffer).decode('utf-8')

    # Send back the annotated frame to the frontend
    emit('response_frame', {'frame': 'data:image/jpeg;base64,' + frame_b64})

    time.sleep(0.05)

if __name__ == '__main__':
    socketio.run(app, debug=True)
