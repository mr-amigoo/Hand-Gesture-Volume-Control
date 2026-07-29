import cv2
import mediapipe as mp
import math
import numpy as np
import os

# 1. Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# 2. Function to set macOS system volume via AppleScript (0 to 100 scale)
def set_mac_volume(volume_percent):
    volume_percent = max(0, min(100, int(volume_percent)))
    os.system(f"osascript -e 'set volume output volume {volume_percent}'")

# 3. Start Video Capture
cap = cv2.VideoCapture(0)

# Variables for UI rendering
vol_bar = 400
vol_percentage = 0

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # MediaPipe requires RGB images
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmark skeletal connections
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract coordinates for Thumb Tip (Landmark 4) and Index Finger Tip (Landmark 8)
            landmarks = hand_landmarks.landmark
            h, w, c = img.shape
            
            x1, y1 = int(landmarks[4].x * w), int(landmarks[4].y * h)
            x2, y2 = int(landmarks[8].x * w), int(landmarks[8].y * h)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # Visual markers on finger tips and connecting line
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Calculate Euclidean distance between fingertips
            length = math.hypot(x2 - x1, y2 - y1)

            # Map pixel distance [30 to 200] directly to macOS volume percentage [0 to 100]
            vol_percentage = np.interp(length, [30, 200], [0, 100])
            vol_bar = np.interp(length, [30, 200], [400, 150])

            # Apply volume setting on macOS
            set_mac_volume(vol_percentage)

            # Visual indicator when pinched closed (Mute/Min Volume)
            if length < 30:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    # Draw Volume Bar UI frame
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(vol_percentage)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Volume Control (macOS)", img)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()