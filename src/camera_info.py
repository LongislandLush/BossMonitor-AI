import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print("Camera opened successfully")
print(f"Width : {width}")
print(f"Height: {height}")
print(f"FPS   : {fps}")

frame_count = 0
start_time = time.time()

while frame_count < 30:
    ret, frame = cap.read()
    if not ret:
        print("Frame read failed!")
        break

    frame_count += 1

end_time = time.time()
elapsed = end_time - start_time

print(f"Captured frames: {frame_count}")
print(f"Elapsed time   : {elapsed:.2f} sec")
print(f"Actual FPS     : {frame_count / elapsed:.2f}")

cap.release()