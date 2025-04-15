import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

# Initialize mediapipe face detection
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to process each frame and detect facial landmarks
def detect_face_attributes(frame):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)
    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_CONTOURS)
    return frame

# Streamlit UI
st.title("Real-time Facial Attribute Detection")
st.subheader("Using your webcam")

# Start webcam stream
cap = cv2.VideoCapture(0)

# Check if webcam is accessible
if not cap.isOpened():
    st.error("Webcam not accessible")
else:
    stframe = st.empty()  # Create a placeholder for displaying the video
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame")
            break

        # Process the frame to detect facial landmarks
        processed_frame = detect_face_attributes(frame)

        # Convert the processed frame to RGB for Streamlit
        processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

        # Display the processed frame in the Streamlit app with use_container_width
        stframe.image(processed_frame_rgb, channels="RGB", use_container_width=True)

    # Release the webcam when the app is stopped
    cap.release()
