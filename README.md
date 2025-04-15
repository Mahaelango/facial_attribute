# **Real-Time Facial Attribute Detection using Streamlit**

This project showcases a lightweight, real-time facial attribute detection system using **MediaPipe** and **Streamlit**, all running on your local webcam — without relying on any pre-trained deep learning models or external downloads.

## **🔍 Features**
- Real-time face detection and facial landmark tracking (eyes, nose, lips, jawline, etc.).
- Webcam integration via OpenCV.
- Simple and fast deployment using Streamlit.
- No external model downloads required.

## **🛠️ Tech Stack**
- **Streamlit** – UI framework for interactive web apps.
- **MediaPipe** – Face Mesh model for facial landmark detection.
- **OpenCV** – Access webcam and image processing.
- **Pillow** – Image conversion for Streamlit display.
- **NumPy** – For efficient matrix operations.

## **📦 Requirements**
Install the following Python libraries:

```bash
pip install streamlit mediapipe opencv-python pillow numpy
```

## **🚀 Getting Started**

1. Clone this repository or copy the `app.py` file to your project.
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Allow webcam permissions if prompted.
4. You’ll see the webcam feed with facial landmarks plotted in real time.

## **🧠 How it Works**
- The webcam feed is captured using OpenCV.
- Each frame is passed to **MediaPipe's FaceMesh** detector.
- It returns 468 facial landmarks which are plotted directly on the video frame.
- The result is streamed live using Streamlit.
