from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
from collections import deque
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Load the trained model
model = load_model('hand_keypoints_model_v2.keras')

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def extract_hand_keypoints(results):
    lh = np.zeros(21*3)
    rh = np.zeros(21*3)
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[idx].classification[0].label
            if hand_label == 'Left':
                lh = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten()
            else:
                rh = np.array([[res.x, res.y, res.z] for res in hand_landmarks.landmark]).flatten()
    return np.concatenate([lh, rh])

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_detection')
def start_detection():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Initialize variables for tracking signs
    buffer = deque(maxlen=20)  # 2 seconds of frames at 10 FPS
    current_sign = None
    current_sign_start_time = None
    detected_word = ""

    # Initialize MediaPipe Hands model
    with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Process the frame and extract keypoints
            image, results = mediapipe_detection(frame, hands)
            keypoints = extract_hand_keypoints(results)

            # If keypoints are detected
            if np.any(keypoints):
                # Reshape keypoints for prediction
                keypoints = keypoints.reshape(1, -1, 1)
                
                # Make prediction
                prediction = model.predict(keypoints)
                predicted_class = np.argmax(prediction)
                confidence = np.max(prediction)

                # Get the class label from the label map
                label_map_inv = {num: label for label, num in label_map.items()}
                predicted_label = label_map_inv[predicted_class]

                # Add prediction to buffer
                buffer.append(predicted_label)

                # Check if the sign has been consistent for 2 seconds
                if len(buffer) == 20 and len(set(buffer)) == 1:  # Same sign for 20 frames
                    if current_sign != predicted_label:
                        current_sign = predicted_label
                        current_sign_start_time = time.time()
                    elif time.time() - current_sign_start_time >= 2:
                        detected_word += current_sign + " "
                        buffer.clear()
                else:
                    current_sign = None
                    current_sign_start_time = None

                # Emit the detected sign and word to the frontend
                socketio.emit('update', {'sign': predicted_label, 'confidence': confidence, 'word': detected_word})

            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display the frame
            cv2.imshow('Live Sign Language Detection', frame)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    socketio.run(app, debug=True)
