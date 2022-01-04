import psutil
from model.scripts.engine_speak import engine_speak

def close_file(voice_data):
    terms = voice_data.split()[1:]
    for file in terms:
        if file == 'lol' or file == "league of legends":
            for process in (process for process in psutil.process_iter() if process.name()=="LeagueClient.exe"):
                process.kill()
            engine_speak("Fechando: League of legends")
        if file == 'tarkov':
            for process in (process for process in psutil.process_iter() if process.name()=="BSGLAUNCHER.exe"):
                process.kill()
            engine_speak("Fechando: Tarkov")
        if file == "gta5" or file =="gta":
            for process in (process for process in psutil.process_iter() if process.name()=="GTA5.exe"):
                process.kill()
            engine_speak("Fechando: GTA 5")
        if file == "discord" or file =="disc":
            for process in (process for process in psutil.process_iter() if process.name()=="Discord.exe"):
                process.kill()
            engine_speak("Fechando: Discord")
        if file == "opera" or file =="navegador" or file=="ópera":
            for process in (process for process in psutil.process_iter() if process.name()=="opera.exe"):
                process.kill()
            engine_speak("Fechando: Opera GX")
        if file == "steam":
            for process in (process for process in psutil.process_iter() if process.name()=="steam.exe"):
                process.kill()
            engine_speak("Fechando: Steam")
        if file == "vscode" or file == "visual studio" or file =="vs code":
            for process in (process for process in psutil.process_iter() if process.name()=="code.exe"):
                process.kill()
            engine_speak("Fechando: VS Code")