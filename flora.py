import speech_recognition as sr
import random
import pyttsx3 
from model.recognize_storage.search_storage import SEARCH_STORAGE
from model.recognize_storage.greeting_storage import GREETINGS
from model.recognize_storage.conversations_storage import CONVERSATION_1, CONVERSATION_2, CONVERSATION_3
from model.recognize_storage.open_storage import OPEN_STORAGE
from model.scripts.greetings import response_greetings, response_conversation
from model.scripts.open_file import open_file
from model.scripts.engine_speak import engine_speak
from model.scripts.search import search_google, search_youtube

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
                engine_speak(ask)
            audio = self.recognize_voice.listen(source, 5, 5)
            try:
                self.voice_data = self.recognize_voice.recognize_google(audio,language='pt-BR')
            except sr.UnknownValueError: #Exceção para caso não fale nada ou não entenda o que foi dito
                engine_speak(f"Desculpe {self.person}, eu não entendi o que você disse, pode repetir?")
            except sr.RequestError:
                engine_speak("Desculpe, meu servidor está off")    
            print(">>", self.voice_data.lower())
            self.voice_data = self.voice_data.lower()
            return self.voice_data.lower()
        
    
    def there_exist(self, terms):
        """ Identificação da existencia dos termos na fala """
        for term in terms:
            if term in self.voice_data:
                return True
            
    
    def response_audio(self, voice_data):
        if self.there_exist(GREETINGS):
           response_greetings(voice_data, self.person)
            
        if self.there_exist(CONVERSATION_1):
           response_conversation(voice_data, 1, self.person)
        
        if self.there_exist(CONVERSATION_2):
            response_conversation(voice_data, 2, self.person)
            
        if self.there_exist(CONVERSATION_3):
            response_conversation(voice_data, 3, self.person)
        #Procurar no google
        if self.there_exist(SEARCH_STORAGE) and 'youtube' not in voice_data:
            search_google(voice_data)
        #Procurar no youtube
        if self.there_exist(SEARCH_STORAGE) and 'youtube' in voice_data:
           search_youtube(voice_data)
        #Abrir programas
        if self.there_exist(OPEN_STORAGE):
            open_file(voice_data)
            
            
    
    def stop_assistant(self):
        if self.there_exist(['sair', 'tchau']):
            engine_speak(f"Tchau {self.person}, foi um prazer falar com você")
            return True
            
            