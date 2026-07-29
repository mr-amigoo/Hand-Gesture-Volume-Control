# 🖐️ Hand Gesture Recognition for Smart Volume Control

## 📌 Project Overview
This project is a real-time computer vision system developed during my 5th semester. It translates hand gestures into device volume commands using a standard webcam, eliminating the need for physical hardware interaction. 

*Note: The original Python source code for this project was unfortunately lost, but this repository serves as a technical breakdown of the system architecture, methodology, and tools used to build it.*

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV
* **Tracking & Landmarks:** MediaPipe
* **Math/Logic:** NumPy 

## 🚀 Key Features
* **Real-Time Tracking:** Utilized MediaPipe’s robust hand-tracking models to map 21 3D hand landmarks in real-time.
* **Dynamic Distance Calculation:** Computed the Euclidean distance between the thumb tip and index finger tip to determine the intended volume level.
* **Smooth Audio Mapping:** Mapped the physical distance between fingers linearly to the system's volume range, allowing for smooth, intuitive audio adjustments.
* **Lightweight Pipeline:** Engineered to run efficiently on standard hardware via a live webcam feed using OpenCV.

## 🧠 System Architecture & How It Worked
1. **Video Capture:** OpenCV captures live frames from the system's webcam.
2. **Color Conversion:** Frames are converted from BGR to RGB as required by MediaPipe.
3. **Landmark Detection:** MediaPipe processes the RGB frame to detect hands and extract the coordinates of 21 specific landmarks.
4. **Distance Measurement:** The system isolates Landmark 4 (Thumb Tip) and Landmark 8 (Index Finger Tip) and calculates the hypotenuse between them.
5. **Command Execution:** The calculated distance is passed through a conversion function (using `pycaw` or similar audio libraries) to adjust the master volume of the operating system instantly.

## 📈 Learnings & Future Scope
Building this system was a significant milestone in my AI and Data Science journey. It provided hands-on experience with live video processing pipelines and spatial coordinate mapping. 

If I were to rebuild this project today, I would:
* Add multi-hand support to control different media functions (e.g., left hand for brightness, right hand for volume).
* Implement a smoothing filter (like a Kalman filter) to reduce volume jittering caused by minor webcam frame drops.
