import os
from model.scripts.engine_speak import engine_speak

def open_file(voice_data):
    terms = voice_data.split()[1:]
    for file in terms:
        if file == 'lol' or file == "league of legends":
            os.startfile(r"M:\Riot Games\League of Legends\LeagueClient.exe")
            engine_speak("Abrindo: League of legends")
        if file == 'tarkov':
            os.startfile(r'D:\BsgLauncher\BsgLauncher.exe')
            engine_speak("Abrindo: Tarkov")
        if file == "gta5" or file =="gta":
            os.startfile(r"D:\SteamLibrary\steamapps\common\Grand Theft Auto V\GTA5.exe")
            engine_speak("Abrindo: GTA 5")
        if file == "discord" or file =="disc":
            os.startfile(r"C:\Users\ERIKFERNANDOMENDESSI\AppData\Local\Discord\app-1.0.9003\Discord.exe")
            engine_speak("Abrindo: Discord")
        if file == "opera" or file =="navegador" or file=="ópera":
            os.startfile(r"C:\Users\ERIKFERNANDOMENDESSI\AppData\Local\Programs\Opera GX\launcher.exe")
            engine_speak("Abrindo: Opera GX")
        if file == "steam":
            os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
            engine_speak("Abrindo: Steam")
        if file == "vscode" or file == "visual studio" or file =="vs code":
            os.startfile(r"C:\Users\ERIKFERNANDOMENDESSI\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            engine_speak("Abrindo: VS Code")
