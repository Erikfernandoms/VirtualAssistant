from model.scripts.engine_speak import engine_speak
from model.scripts.period import get_period
import random

def response_greetings(voice_data, person):
    rand = random.randint(0,2)
    if rand == 1:
        greetings = [f'Olá {person}, como você está',
                    f'Oi {person}, como posso ajudar você?']
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)
    else:
        if get_period() == 'dia':
            greetings = [f'Bom dia {person}, tudo bem com você?', f'Bom dia {person}, como posso ser útil hoje?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            engine_speak(greet)
        elif get_period() == 'tarde':
                greetings = [f'Boa tarde {person}, tudo bem com você?', f'Boa tarde {person}, como posso ser útil hoje?']
                greet = greetings[random.randint(0, len(greetings)-1)]
                engine_speak(greet)
        else:
            greetings = [f'Boa noite {person}, tudo bem com você?', f'Boa noite {person}, como posso ser útil hoje?']
            greet = greetings[random.randint(0, len(greetings)-1)]
            engine_speak(greet)
            

def response_conversation(voice_data, conversation, person):
    if conversation == 1:
        greetings = ['estou bem sim e você?', 'tudo perfeitamente em ordem e por ai?', 'bão demais e com você?']
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)
    elif conversation == 2:
        greetings = ['Sempre bem, obrigada por perguntar', 'Estou maravilhosa', 'A pergunta é: quando que não estou? kkk']
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)
    else:
        greetings = [f'Que bom {person}, fico feliz! Em que posso ajudar?', 'Ótimo, posso ajudar em algo?']
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)
                