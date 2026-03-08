# SigmaOutsiderCapture

This is a security script for Windows that captures a photo using the webcam when someone fails a login attempt.

# How it works

When someone tries to log in to your computer and fails, the script *takes a photo* and saves it in a folder called "Captures".
If someone failed the login, the next time you log in you will *receive a notification* informing you.

The program is based on Windows Tasks to capture specific events such as:
  1. Event ID *4625*: Triggered on a failed login.
  2. Event ID *4624*: Triggered on a successful login.

# Compiling

*Install the libraries*

`pip install opencv-python win10toast-click`

*PyInstaller*

`python -m PyInstaller --onedir --noconsole --uac-admin --hidden-import win10toast_click --collect-all win10toast_click --icon="icon.ico" --name SigmaOutsiderCapture pr.py`

# Why I made the script

I made this script because I wanted more privacy by knowing if someone tries to enter my PC. When I searched for these kinds of programs, I found that I needed a subscription for most of them, and since I couldn't see the source code, I couldn't trust where my photos were being saved.
