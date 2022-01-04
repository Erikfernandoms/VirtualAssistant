import speech_recognition as sr
import pyttsx3, random
from model.recognize_storage.close_storage import CLOSE_STORAGE
from model.recognize_storage.computer_manager_storage import TURN_OFF,RESTART
from model.recognize_storage.weather_storage import WHEATER_CONVERSATION
from model.recognize_storage.introduction_storage import INTRODUCTION, INTRODUCTION_MESTRE
from model.recognize_storage.search_storage import SEARCH_STORAGE
from model.recognize_storage.greeting_storage import GREETINGS
from model.recognize_storage.conversations_storage import CONVERSATION_1, CONVERSATION_2, CONVERSATION_3, CONVERSATION_4
from model.recognize_storage.open_storage import OPEN_STORAGE
from model.recognize_storage.operations_storage import SUM,SUB,MULT,DIV,POW
from model.scripts.close_file import close_file
from model.scripts.greetings import response_greetings, response_conversation
from model.scripts.open_file import open_file
from model.scripts.engine_speak import engine_speak
from model.scripts.search import search_google, search_youtube
from model.scripts.calculator import calculator
from model.scripts.there_exist import there_exist
from model.scripts.get_weather import get_weather, get5days_weather, get_local_code, search_local
from model.scripts.computer_management import shutdown,restart


class Virtual_assistant():
    def __init__(self):
        self.person = "" #Pessoa que estará falando com a assistente
        self.assistant_name = "Flora"#Nome da assistente
        
        self.engine = pyttsx3.init() #Conversão de texto para fala
        self.recognize_voice = sr.Recognizer() #Reconhecimento da fala
        
        self.voice_data = ''

    def introduction(self):
        engine_speak("Olá aqui é a Flora, com quem estou falando?")
        
    def person_name(self, voice_data):
        if there_exist(voice_data, INTRODUCTION_MESTRE):
            boss_names = ['Sr. Erik', 'Mestre', 'Chefe']
            self.person = boss_names[random.randint(0, len(boss_names)-1)]
            responses = [f'Desculpe {self.person}, seja bem vindo de volta! Posso fazer algo?', f'Perdão {self.person}, tudo bem com você?', f'Bem vindo de volta {self.person}']
            flora_responses = responses[random.randint(0,len(responses)-1)]
            engine_speak(flora_responses)
        elif there_exist(voice_data,INTRODUCTION):
            person_name = voice_data.split()[-1]
            self.person = person_name
            engine_speak(f"Seja bem vindo {self.person}, o que posso fazer por você hoje?")
        else:
            person_name = voice_data
            self.person = person_name
            engine_speak(f"Seja bem vindo {self.person}, como posso ajudar você?")     
               
    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                engine_speak(ask)
            audio = self.recognize_voice.listen(source, timeout=None, phrase_time_limit=None)
            try:
                self.voice_data = self.recognize_voice.recognize_google(audio,language='pt-BR')
            except sr.UnknownValueError: #Exceção para caso não fale nada ou não entenda o que foi dito
                engine_speak(f"Desculpe {self.person}, eu não entendi o que você disse, pode repetir?")
            except sr.RequestError:
                engine_speak("Desculpe, meu servidor está off")    
            print(">>", self.voice_data.lower())
            self.voice_data = self.voice_data.lower()
            return self.voice_data.lower()   
            
    
    def response_audio(self, voice_data):
        if there_exist(voice_data,GREETINGS):
           response_greetings(voice_data, self.person)
            
        if there_exist(voice_data,CONVERSATION_1):
           response_conversation(voice_data, 1, self.person)
        
        if there_exist(voice_data,CONVERSATION_2) and 'você' in voice_data:
            response_conversation(voice_data, 2, self.person)
            
        if there_exist(voice_data,CONVERSATION_3):
            response_conversation(voice_data, 3, self.person)
        
        if there_exist(voice_data,CONVERSATION_4):
            response_conversation(voice_data, 4, self.person)
        
        #Procurar no google
        if there_exist(voice_data,SEARCH_STORAGE) and 'youtube' not in voice_data:
            search_google(voice_data)
        #Procurar no youtube
        if there_exist(voice_data,SEARCH_STORAGE) and 'youtube' in voice_data:
           search_youtube(voice_data)
        #Abrir programas
        if there_exist(voice_data,OPEN_STORAGE):
            open_file(voice_data)
        #Fechar programas
        if there_exist(voice_data,CLOSE_STORAGE):
            close_file(voice_data)
        #Calculadora
        if there_exist(voice_data,['calcule','calcular']):
            if there_exist(voice_data,SUM):
                calculator(voice_data,"+")
            elif there_exist(voice_data,SUB):
                calculator(voice_data, "-")
            elif there_exist(voice_data,MULT):
                calculator(voice_data, "*")
            elif there_exist(voice_data,DIV):
                calculator(voice_data,"/")
            elif there_exist(voice_data,POW):
               calculator(voice_data, "**")
            else:
                engine_speak("Desculpe, não entendi.")
        #Previsão do tempo        
        if there_exist(voice_data, WHEATER_CONVERSATION):
            response = voice_data.split()[4:-1]
            local = ' '.join(response)
            get_weather(local)
            engine_speak("Deseja ver a previsão para os próximos dias? ")
            answer = self.record_audio()
            if answer == 'sim':
                coord = search_local(local)
                code = get_local_code(coord['lat'], coord['long'])
                days_weather = get5days_weather(code['codigoLocal'])
                for day in days_weather:
                    engine_speak("Previsão para:" + day['dia'] + ': ' + day['clima'])
                    engine_speak('Mínima: ' + str(int(day['min'])) + "\xb0" + "C, Máxima:" + str(int(day['max'])) + "\xb0" + "C")
            else:
                engine_speak(f"Tudo bem {self.person}, mais alguma coisa?")
        #Desligar o computador
        if there_exist(voice_data, TURN_OFF):
            engine_speak("Você tem certeza que quer desligar o computador?")
            answer = self.record_audio()
            if answer == 'sim':
                shutdown()
            else:
                engine_speak(f"Tudo bem {self.person}, mais alguma coisa?")
        #Reiniciar o computador
        if there_exist(voice_data, RESTART):
            engine_speak("Você tem certeza que quer reiniciar o computador?")
            answer = self.record_audio()
            if answer == 'sim':
                restart()
            else:
                engine_speak(f"Tudo bem {self.person}, mais alguma coisa?")
        
    
    def stop_assistant(self):
        if there_exist(self.voice_data,['sair', 'tchau', 'por hora só']):
            engine_speak(f"Tchau {self.person}, foi um prazer falar com você")
            return True
            
            