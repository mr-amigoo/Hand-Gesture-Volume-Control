# 🖐️ Hand Gesture Recognition for Smart Volume Control

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.0-orange)
![Platform](https://img.shields.io/badge/Platform-macOS-lightgrey)

## 📌 Project Overview
A real-time computer vision system that translates physical hand gestures into system volume commands. By utilizing a standard webcam, this project maps spatial landmark coordinates to the macOS master volume, allowing users to control their audio intuitively without touching a keyboard or mouse.

Originally built during my 5th semester, this repository contains the modernized, lightweight macOS implementation of the pipeline.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV
* **Tracking & Landmarks:** Google MediaPipe (Hands)
* **Math/Logic:** NumPy
* **System Control:** AppleScript (`osascript`) via Python `os` module

## 🚀 Key Features
* **Real-Time Tracking:** Utilizes MediaPipe’s robust machine learning models to map 21 3D hand landmarks in real-time.
* **Dynamic Distance Calculation:** Computes the Euclidean distance between the thumb tip and index finger tip.
* **Smooth Audio Mapping:** Maps the pixel distance linearly to the macOS volume range (0-100%) for smooth, intuitive audio adjustments.
* **macOS Native Integration:** Bypasses heavy third-party audio libraries by directly triggering native AppleScript volume commands.
* **Visual UI Overlay:** Renders a live volume bar and percentage indicator directly on the video feed.

## 🧠 System Architecture
1. **Video Capture:** OpenCV captures live frames from the webcam.
2. **Color Conversion:** Frames are converted from BGR to RGB (MediaPipe requirement).
3. **Landmark Detection:** MediaPipe processes the RGB frame to detect hands and extract 21 specific landmark coordinates.
4. **Distance Measurement:** The system isolates Landmark 4 (Thumb Tip) and Landmark 8 (Index Finger Tip) and calculates the hypotenuse between them.
5. **Command Execution:** The calculated distance is mapped to a percentage and passed to the macOS terminal via `osascript`, instantly adjusting the system volume.

## 💻 Installation & Setup (macOS)

### Prerequisites
* Python 3.8+
* A working webcam

### 1. Clone the Repository
```bash
git clone [https://github.com/mr-amigoo/Hand-Gesture-Volume-Control.git](https://github.com/mr-amigoo/Hand-Gesture-Volume-Control.git)
cd Hand-Gesture-Volume-Control
