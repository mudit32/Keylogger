# Cybersecurity Monitoring and Awareness System

## Overview

This project is an educational cybersecurity demonstration tool developed in Python to showcase how monitoring software can collect system activity data and how such behavior can be detected and mitigated. The project is intended solely for learning, research, and cybersecurity awareness purposes in authorized environments.

## Features

* **Keyboard Activity Logging**

  * Records keyboard events with timestamps.
  * Stores captured events in a local log file.

* **Screen Recording**

  * Captures desktop activity in real time.
  * Saves recordings as a video file.

* **Camera Monitoring**

  * Records webcam footage.
  * Stores captured video locally.

* **Automated Reporting**

  * Sends generated reports and recordings via email.
  * Demonstrates how data transfer mechanisms can be used in monitoring applications.

* **Security Awareness Module**

  * Displays cybersecurity awareness tips.
  * Educates users about common defensive measures.

## Technologies Used

* Python
* OpenCV
* NumPy
* PyAutoGUI
* Pynput
* Tkinter
* SMTP (Email Services)
* Multithreading

## Project Structure

```
project/
│
├── main.py
├── keys.txt
├── screen.avi
├── camera.avi
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-folder>
```

2. Install dependencies:

```bash
pip install opencv-python numpy pyautogui pynput
```

3. Run the application:

```bash
python main.py
```

## Workflow

1. Start the application.
2. Monitoring modules run concurrently using threads.
3. Activity data is collected and stored locally.
4. Generated reports can be sent through email.
5. The awareness module displays cybersecurity recommendations.

## Learning Objectives

* Understand multithreaded application development.
* Learn real-time data collection techniques.
* Explore security monitoring concepts.
* Study defensive cybersecurity practices.
* Understand the importance of system permissions and endpoint security.

## Defensive Recommendations

* Use reputable antivirus and anti-malware software.
* Monitor application permissions regularly.
* Restrict unnecessary camera and microphone access.
* Keep operating systems and applications updated.
* Use firewalls and intrusion detection systems.
* Avoid installing software from untrusted sources.

## Disclaimer

This project is intended strictly for educational, research, and cybersecurity awareness purposes in systems where you have explicit authorization. Users are responsible for complying with all applicable laws, regulations, and organizational policies. Unauthorized monitoring of devices, networks, or individuals may be illegal and unethical.
