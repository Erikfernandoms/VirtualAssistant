from playsound import playsound
from gtts import gTTS 
import os, random 


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='pt')
    rand = random.randint(1,20000)
    audio_file = 'audio' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print('Flora: ' + audio_string)
    os.remove(audio_file)