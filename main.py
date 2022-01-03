from flora import Virtual_assistant

assistant = Virtual_assistant()
assistant.introduction()
voice_data = assistant.record_audio()
assistant.person_name(voice_data)
while True:
    
    voice_data = assistant.record_audio()
    assistant.response_audio(voice_data)
    
    if assistant.stop_assistant():
        break