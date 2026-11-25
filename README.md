# WSL System Monitor CLI

A lightweight, real-time terminal dashboard built in Python to monitor CPU load, memory usage, disk space, and active processes inside a Windows Subsystem for Linux (WSL2) environment.

## Features
- **Live Terminal UI:** Updates metrics in-place every second using `rich`.
- **Linux Kernel Metrics:** Reads real-time resource stats via `psutil`.
- **Clean Signal Handling:** Gracefully handles `SIGINT` (`Ctrl+C`) exits.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com<YOUR-USERNAME>/wsl-sysmon.git
   cd wsl-sysmon
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the monitor:**
   ```bash
   python3 monitor.py
   ```
