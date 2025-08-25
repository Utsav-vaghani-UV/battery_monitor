# Battery Monitor

A lightweight Python-based Windows application that monitors your laptop battery in real-time. It provides popup alerts when the battery is **low** or **fully charged** and runs in the background with minimal memory usage.

---

## Features

- **Popup Alerts**
  - Battery ≥ 98% while charging → “Turn off charging”
  - Battery ≤ 30% while not charging → “Start charging”
- **Startup Notification**: Shows “Battery Monitor is started” when the app runs.
- **Automatic Exit**: Closes when the charger is unplugged, optionally shows a “stopped” popup.
- **Lightweight**: Minimal memory usage (~20–25 MB) with no heavy GUI frameworks.
- **Runs in Background**: Can be set to start automatically on Windows startup.

---

## Prerequisites

- Windows 10/11
- Python 3.12+ (for running from source)
- [psutil](https://pypi.org/project/psutil/) (for battery monitoring)
- `pyinstaller` (for creating `.exe`)

---

## Installation

### 1. Clone the repository
```bash
git clone <https://github.com/Utsav-vaghani-UV/battery_monitor>
cd BatteryMonitor
```
## Terminal codes
```bash
python -m venv .venv
.\.venv\Scripts\activate

pip install psutil pyinstaller

pip install -r requirements.txt

EXECUTION_PART
python battery_monitor.py

pyinstaller --noconsole --onefile battery_monitor.py
```

## You can find the exe file in: dist\battery_monitor.exe
