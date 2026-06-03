import cv2
import time
from datetime import datetime
from pathlib import Path

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

output_dir = Path("../event_images")
output_dir.mkdir(exist_ok=True)

ret, prev_frame = cap.read()

if not ret:
    print("Initial frame capture failed!")
    cap.release()
    exit()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

print("Motion detection started. Press Ctrl+C to stop.")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Frame read failed!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(
            thresh.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) < 1500:
                continue

            motion_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if motion_detected:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = output_dir / f"motion_{timestamp}.jpg"
            cv2.imwrite(str(filename), frame)
            print(f"Motion detected! Saved: {filename}")
            time.sleep(1)

        prev_gray = gray
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Motion detection stopped by user.")

cap.release()