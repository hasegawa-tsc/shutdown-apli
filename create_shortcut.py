import os
import winshell
from win32com.client import Dispatch

def create_shortcut():
    desktop = winshell.desktop()
    path = os.path.join(desktop, "shutdown_apli.lnk")
    target = os.path.abspath(os.path.join("dist", "shutdown_apli.exe"))
    wDir = os.path.abspath("dist")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.save()
    print(f"Shortcut created at: {path}")

if __name__ == "__main__":
    create_shortcut()
