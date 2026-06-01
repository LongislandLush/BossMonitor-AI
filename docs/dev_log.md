# Development Log

---

# 2026/05/18

## Repository Initialization

- Created BossMonitor-AI GitHub repository
- Connected local VS Code project with GitHub
- Added project directory structure
- Added README architecture and roadmap
- Initialized documentation folders
- Added initial Git commit structure

## Notes

Learned basic Git workflow:

```bash
git add .
git commit
git push
```

Started using Conventional Commit style.

---

# 2026/05/28

## Orange Pi Zero Camera Bring-up

### Hardware

- Orange Pi Zero
- Logitech C270 USB Webcam

### Progress

- Booted Armbian Linux successfully
- Verified USB webcam detection
- Verified V4L2 device initialization
- Installed `fswebcam`
- Successfully captured first image (`test.jpg`)

### Commands Learned

```bash
dmesg | tail
ls /dev/video*
v4l2-ctl --list-devices
fswebcam test.jpg
```

### Important Findings

#### Logitech C270 detected successfully

```text
Found UVC 1.00 device C270 HD WEBCAM
```

#### V4L2 devices initialized

```text
/dev/video0
/dev/video1
```

#### Warning observed

```text
cannot set freq 24000 to ep 0x82
```

This appears related to the webcam audio endpoint and does not affect image capture.

## Current Status

Phase 1 - SBC Camera Bring-up:
SUCCESS

# 2026/06/01

## OpenCV Bring-up

### Progress

- Installed OpenCV 4.6.0 on Orange Pi Zero
- Verified cv2 module installation
- Successfully opened Logitech C270 using OpenCV
- Captured image using Python
- Saved image as capture.jpg

### Commands Learned

```bash
python3 camera_test.py
```

### Notes

Observed GStreamer warning:

```text
GStreamer: pipeline have not been created
```

The warning did not affect image capture.
OpenCV successfully fell back to V4L2 and saved capture.jpg.

### Status

Phase 2 - OpenCV Camera Control:
SUCCESS