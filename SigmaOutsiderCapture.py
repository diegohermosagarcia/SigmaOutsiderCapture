import cv2,os,sys,subprocess,time
from datetime import datetime
from win10toast_click import ToastNotifier
from pathlib import Path

# folders and tasknames config
mainDir = Path(sys.executable).parent
capsDir = mainDir / "Captures"
lastCheckFile = mainDir / "lastCheck.dat"
nameCapTask = "SigmaOutsiderCapture_Cap"
nameAdviceTask = "SigmaOutsiderCapture_Advice"
caps= 3 # how many caps do you want to take

def openFolder():
    if capsDir.exists():
        os.startfile(str(capsDir))

        with open(lastCheckFile, "w") as f:
            f.write(str(time.time()))

def createTasks():
    """Creation of the tasks. You must run as Admin!"""
    doc = Path(sys.executable).absolute()
    baseCommand = f'"{doc}"'

    # Capture task
    cmdCap = f'schtasks /create /tn "{nameCapTask}" /tr "{baseCommand} -modeCap" /sc ONEVENT /ec Security /mo "*[System[(EventID=4625)]]" /rl HIGHEST /ru "SYSTEM" /f'

    
    # Notify task
    cmdAdvice = f'schtasks /create /tn "{nameAdviceTask}" /tr "{baseCommand} -modeNotif" /sc ONEVENT /ec Security /mo "*[System[(EventID=4624)]]" /rl HIGHEST /f'
    
    try:

        subprocess.run(cmdCap, shell=True)
        subprocess.run(cmdAdvice, shell=True)
        print(f"-> {nameCapTask} successfully installed on: {mainDir}")
    except:
        print(f"-> The program wasnt installed, you probably are not executing the program as an admin")

def capture():
    """This function makes intruders lose their aura"""
    if not capsDir.exists():
        capsDir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        #I cant access to the camera ;(
        exit()
    
    for i in range(caps):

        time.sleep(3) 
        ret, frame = cap.read()
        if ret:
            ts = datetime.now().strftime('%Y%m%d_%H%M%S')
            cv2.imwrite(str(capsDir / f"outsider_{ts}.jpg"), frame)

        time.sleep(0.5) 

    cap.release()

def notify():
    if not capsDir.exists() or not any(capsDir.iterdir()):
        return

    lastCheckTime = 0
    if lastCheckFile.exists():
        with open(lastCheckFile, "r") as f:
            try:
                lastCheckTime = float(f.read().strip())
            except:
                lastCheckTime = 0

    newCaps = []
    for photo in capsDir.iterdir():
        if photo.stat().st_mtime > lastCheckTime:
            newCaps.append(photo.name)

    if newCaps:
        toaster = ToastNotifier()
        toaster.show_toast(
            "SigmaOutsiderCapture",
            f"Found {len(newCaps)} new intruders. Click here to check and mute.",
            duration=10,
            callback_on_click=openFolder
        )

        time.sleep(20)

if __name__ == "__main__":
    #commands used by windows tasks
    if "-modeCap" in sys.argv:
        capture()
    elif "-modeNotif" in sys.argv:
        notify()
    else:
        #first execution or manual (create the tasks)
        createTasks()