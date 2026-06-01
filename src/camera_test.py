import cv2

print("OpenCV Version:", cv2.__version__)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

ret, frame = cap.read()

if ret:
    cv2.imwrite("capture.jpg", frame)
    print("Image saved: capture.jpg")
else:
    print("Capture failed!")

cap.release()
