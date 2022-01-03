from flora import Virtual_assistant

assistant = Virtual_assistant('Flora', 'Erik')

while True:
    voice_data = assistant.record_audio('Ouvindo...')
    assistant.response_audio(voice_data)
    
    if assistant.stop_assistant():
        break