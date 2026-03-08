# SigmaOutsiderCapture

This is a security script for Windows that captures a photo using the webcam when someone fails a login attempt.

# How it works

When someone tries to log in your computer and fails, the script *takes a photo* and saves it on a folder called "Captures".
If someone has failed the login, the next time you log in you would *receive a notification*.

The program is based on Windows Tasks to capture specific events as:
  1.Event ID *4625* : Triggered on a failed login.
  2.Event ID *4624* : Triggered on a successful login.

# Compiling

*Install the libraries*

`pip install opencv-python win10toast-click`

*PyInstaller*

`python -m PyInstaller --onedir --noconsole --uac-admin --hidden-import win10toast_click --collect-all win10toast_click --icon="icon.ico" --name SigmaOutsiderCapture pr.py`

# Why I made the script

I made this script because I wanted more privacy knowing if someone tries to enter my PC but, when I searched for these kinds of programs, I found that I needed a payed subscription for most of them, and as I couldn't see the source code, I couldn't trust where my photos were saved.
