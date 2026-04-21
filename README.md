# Network Scanner CLI

A Command Line Interface (CLI) application built in Python for fast network port scanning using multi-threading. This project is designed with production-grade standards, featuring modular architecture, graceful error handling, and background logging.

## Key Features
* **Blazing Fast:** Utilizes `ThreadPoolExecutor` to scan hundreds of ports concurrently.
* **Smart Validation:** Automatically resolves Domain names to IP Addresses before scanning.
* **Lightweight & Secure:** Built entirely with Python's standard library. Zero external dependencies required.
* **Activity Logging:** Automatically records errors and scan history into a `network_scanner.log` file.

## Prerequisites
* Python 3.7 or higher.

## Installation
1. Clone this repository or download the source code:
   ```bash
   git clone [https://github.com/yourusername/network-scanner-cli.git](https://github.com/yourusername/network-scanner-cli.git)
   cd network-scanner-cli ```

2. (Optional) Create and activate a Virtual Environment:
    ```bash
    python -m venv venv
    
    # For Linux/macOS
    source venv/bin/activate  
    
    # For Windows
    venv\Scripts\activate ```

## Usage Guide
* Use main.py as the entry point of the application.

1. Display the Help Menu:
    ```bash
    python main.py --help ```

2. Scan a Target with Default Ports (1-1024):
    ```bash
    python main.py 192.168.1.1 ```

3. Scan a Domain with Specific Ports:
    ```bash
    python main.py scanme.nmap.org -p 80,443,808 ```

4.  Scan a Port Range with Verbose Mode (Detailed output):
    ``` bash
    python main.py 10.0.0.1 -p 1-5000 -v ```

## Legal Disclaimer
*This application is created strictly for Educational Purposes and Ethical Security Auditing. You must only use this tool on systems you own or have explicit written permission to scan. The developer assumes no liability and is not responsible for any misuse, damage, or illegal activities caused by this tool.