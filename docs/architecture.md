# System Architecture

```text
Logitech Webcam
      |
      v
Orange Pi
  - Linux
  - Python
  - OpenCV
  - Image capture
  - Motion detection
      |
      | UART / GPIO
      v
STM32
  - Sensor input
  - LED / buzzer alert
  - Future relay / motor control
```