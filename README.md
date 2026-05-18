# BossMonitor-AI

AI-powered edge monitoring system using Orange Pi, USB webcam, and STM32.

## Hardware

- Orange Pi
- Logitech USB Webcam
- STM32F446RE
- STM32F103C8T6

## System Architecture

```text
Logitech Webcam
      |
      v
Orange Pi
  - Linux
  - Python
  - OpenCV
  - Image capture
  - Motion / person / face detection
      |
      | UART / GPIO / USB Serial
      v
STM32
  - Sensor input
  - LED / buzzer alert
  - Future motor / relay control
```
## Project Structure
```text
BossMonitor-AI/
├─ README.md
├─ docs/
│  ├─ architecture.md
│  ├─ hardware_plan.md
│  └─ dev_log.md
├─ src/
│  ├─ camera_test.py
│  └─ motion_detect.py
├─ stm32/
│  ├─ F446RE/
│  └─ F103C8T6/
├─ scripts/
│  └─ setup_orangepi.sh
└─ hardware/
   └─ wiring_notes.md
```
## Development Roadmap

### Phase 1: SBC Camera Bring-up

- Detect USB webcam on Orange Pi
- Capture image using fswebcam
- Capture image using Python OpenCV

### Phase 2: Basic Vision

- Motion detection
- Person detection
- Face detection experiment

### Phase 3: STM32 Integration

- UART communication between Orange Pi and STM32
- STM32 LED / buzzer alert
- Sensor input support

### Phase 4: Network / Dashboard

- Web dashboard
- Event logging
- Remote notification