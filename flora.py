from math import exp
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS 
import random
import webbrowser
import pyttsx3
import os
from model.recognize_storage.search_storage import SEARCH_STORAGE
from model.recognize_storage.greeting_storage import GREETINGS
from model.recognize_storage.conversations_storage import CONVERSATION_1, CONVERSATION_2, CONVERSATION_3
from model.auxiliar_code.period import get_period
from model.recognize_storage.open_storage import OPEN_STORAGE

class Virtual_assistant():
    def __init__(self, assistant_name, person):
        self.person = person #Pessoa que estará falando com a assistente
        self.assistant_name = assistant_name #Nome da assistente
        
        self.engine = pyttsx3.init() #Conversão de texto para fala
        self.recognize_voice = sr.Recognizer() #Reconhecimento da fala
        
        self.voice_data = ''


    def engine_speak(self, text):
        """ Assistant speak """
        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()
        
        
    def record_audio(self, ask=""):
        with sr.Microphone() as source:
            if ask:
                self.engine_speak(ask)
            audio = self.recognize_voice.listen(source, 5, 5)
            try:
                self.voice_data = self.recognize_voice.recognize_google(audio,language='pt-BR')
            except sr.UnknownValueError: #Exceção para caso não fale nada ou não entenda o que foi dito
                self.engine_speak(f"Desculpe {self.person}, eu não entendi o que você disse, pode repetir?")
            except sr.RequestError:
                self.engine_speak("Desculpe, meu servidor está off")    
            print(">>", self.voice_data.lower())
            self.voice_data = self.voice_data.lower()
            return self.voice_data.lower()
        
        
    def engine_speak(self, audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='pt')
        rand = random.randint(1,20000)
        audio_file = 'audio' + str(rand) + '.mp3'
        tts.save(audio_file)
        playsound(audio_file)
        print(self.assistant_name + ': ' + audio_string)
        os.remove(audio_file)
        
    
    def there_exist(self, terms):
        """ Identificação da existencia dos termos na fala """
        for term in terms:
            if term in self.voice_data:
                return True
            
    
    def response_audio(self, voice_data):
        if self.there_exist(GREETINGS):
            rand = random.randint(0,2)
            if rand == 1:
                greetings = [f'Olá {self.person}, como você está',
                            f'Oi {self.person}, como posso ajudar você?']
                greet = greetings[random.randint(0, len(greetings)-1)]
                self.engine_speak(greet)
            else:
                if get_period() == 'dia':
                    greetings = [f'Bom dia {self.person}, tudo bem com você?', f'Bom dia {self.person}, como posso ser útil hoje?']
                    greet = greetings[random.randint(0, len(greetings)-1)]
                    self.engine_speak(greet)
                elif get_period() == 'tarde':
                    greetings = [f'Boa tarde {self.person}, tudo bem com você?', f'Boa tarde {self.person}, como posso ser útil hoje?']
                    greet = greetings[random.randint(0, len(greetings)-1)]
                    self.engine_speak(greet)
                else:
                    greetings = [f'Boa noite {self.person}, tudo bem com você?', f'Boa noite {self.person}, como posso ser útil hoje?']
                    greet = greetings[random.randint(0, len(greetings)-1)]
                    self.engine_speak(greet)
            
        if self.there_exist(CONVERSATION_1):
            greetings = ['estou bem sim e você?', 'tudo perfeitamente em ordem e por ai?', 'bão demais e com você?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
        
        if self.there_exist(CONVERSATION_2):
            greetings = ['Sempre bem, obrigada por perguntar', 'Estou maravilhosa', 'A pergunta é: quando que não estou? kkk']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
            
        if self.there_exist(CONVERSATION_3):
            greetings = [f'Que bom {self.person}, fico feliz! Em que posso ajudar?', 'Ótimo, posso ajudar em algo?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
                
            
        #Procurar no google
        if self.there_exist(SEARCH_STORAGE) and 'youtube' not in voice_data:
            terms = voice_data.split()[1:]
            search_term = " ".join(terms)
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no google")
            
        #Procurar no youtube
        if self.there_exist(SEARCH_STORAGE) and 'youtube' in voice_data:
            terms = voice_data.split()[1:-2]
            search_term = " ".join(terms)
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no youtube")
            
        #Abrir programas
        if self.there_exist(OPEN_STORAGE):
            terms = voice_data.split()[1:]
            for file in terms:
                if file == 'lol' or file == "league of legends":
                    os.startfile(r'D:\Riot Games\Riot Client\RiotClientServices.exe')
                    self.engine_speak("Abrindo: League of legends")
                if file == 'tarkov':
                    os.startfile(r'D:\BsgLauncher\BsgLauncher.exe')
                    self.engine_speak("Abrindo: Tarkov")