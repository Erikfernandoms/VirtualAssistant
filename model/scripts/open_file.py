import os
from model.scripts.engine_speak import engine_speak

def open_file(voice_data):
    terms = voice_data.split()[1:]
    for file in terms:
        if file == 'lol' or file == "league of legends":
            os.startfile(r'D:\Riot Games\Riot Client\RiotClientServices.exe')
            engine_speak("Abrindo: League of legends")
        if file == 'tarkov':
            os.startfile(r'D:\BsgLauncher\BsgLauncher.exe')
            engine_speak("Abrindo: Tarkov")
    