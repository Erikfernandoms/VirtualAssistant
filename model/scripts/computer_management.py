import os

def shutdown():
    os.system("shutdown /s /t 5")

def restart():
    os.system("shutdown /r /t 5")