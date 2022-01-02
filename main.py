from math import exp
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS 
import random
import webbrowser
import pyttsx3
import os


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
                print("Ouvindo...")
                self.engine_speak(ask)
                
            audio = self.recognize_voice.listen(source, 5, 5)
            print('Verificando o banco de dados')
            
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
        if self.there_exist(['oi', 'olá']):
            greetings = [f'Olá {self.person}, como você está',
                         f'Oi {self.person}, como posso ajudar você?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
        elif self.there_exist(['bom dia']):
            greetings =  [f'Bom dia {self.person}, tudo bem?',f'Bom dia {self.person}, como posso ajudá-lo?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
        elif self.there_exist(['boa tarde']):
            greetings =  [f'Boa tarde {self.person}, tudo bem?',f'Boa tarde {self.person}, como posso ajudá-lo?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
        elif self.there_exist(['boa noite']):
            greetings =  [f'Boa noite {self.person}, tudo bem?',f'Boa noite {self.person}, como posso ajudá-lo?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            self.engine_speak(greet)
            
        #Procurar no google
        if self.there_exist(['pesquise', 'pesquisar', 'procure', 'procurar']) and 'youtube' not in voice_data:
            search_term = voice_data.split()[-1]
            url = "http://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            self.engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no google")
            
        #Procurar no youtube
        if self.there_exist(['pesquise', 'pesquisar', 'procure', 'procurar']) and 'youtube' in voice_data:
            search_term = voice_data.split()[-3]
            url = "https://www.youtube.com/results?search_query=" + search_term
            webbrowser.get().open(url)
            self.engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no youtube")
            
        #Abrir programas
        if self.there_exist(['abrir']):
            pass
        
        
assistant = Virtual_assistant('Flora', 'Erik')

while True:
    voice_data = assistant.record_audio('Ouvindo...')
    assistant.response_audio(voice_data)
    
    if assistant.there_exist(['sair', 'tchau']):
        assistant.engine_speak(f"Tchau {assistant.person}, foi um prazer falar com você")
        break