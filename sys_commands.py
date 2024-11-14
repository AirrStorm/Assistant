import os
import ctypes
from speechrecognitionfunc import listen

def open_browser(command):
    if "browser" in command:
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        return "Browser opened"
    
def open_explorer(command):
    if "file explorer" in command:
        os.startfile("explorer")
        return "File Explorer opened"

def shutdown_system(command):
    if "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "System is shutting down"

def restart_system(command):
    if "restart" in command:
        os.system("shutdown /r /t 1")
        return "System is restarting"

def logoff_system(command):
    if "log off" in command:
        os.system("shutdown /l")
        return "Logging off"

def lock_system(command):
    if "lock system" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "System locked"

def open_notepad(command):
    if "notepad" in command:
        os.startfile("notepad.exe")
        return "Notepad opened"

def open_calculator(command):
    if "calculator" in command:
        os.startfile("calc.exe")
        return "Calculator opened"

def mute_system(command):
    if "mute" in command:
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)  # Mute key code
        return "System volume muted"

def unmute_system(command):
    if "unmute" in command:
        ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)  # Mute key code toggles mute/unmute
        return "System volume unmuted"

def adjust_volume(command):
    if "increase volume" in command:
        for _ in range(5):  # Adjust the range as needed
            ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)  # Volume Up key code
        return "Volume increased"
    elif "decrease volume" in command:
        for _ in range(5):
            ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)  # Volume Down key code
        return "Volume decreased"

def open_control_panel(command):
    if "control panel" in command:
        os.startfile("control.exe")
        return "Control Panel opened"

def open_command_prompt(command):
    if "command prompt" in command:
        os.system("start cmd")
        return "Command Prompt opened"
