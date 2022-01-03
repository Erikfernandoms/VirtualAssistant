from flora import Virtual_assistant

assistant = Virtual_assistant('Flora', 'Erik')

while True:
    voice_data = assistant.record_audio('Ouvindo...')
    assistant.response_audio(voice_data)
    
    if assistant.there_exist(['sair', 'tchau']):
        assistant.engine_speak(f"Tchau {assistant.person}, foi um prazer falar com você")
        break