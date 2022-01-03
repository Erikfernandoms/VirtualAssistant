from model.scripts.engine_speak import engine_speak

def calculator(voice_data, op):
    if op == "+":
        numbers = voice_data.split()
        resultado = int(numbers[1]) + int(numbers[3])
        engine_speak(f"O resultado da soma é: {resultado}")
    if op == "-":
        numbers = voice_data.split()
        resultado = int(numbers[1]) - int(numbers[3])
        engine_speak(f"O resultado da subtração é: {resultado}")
    if op == "/":
        if "por" in voice_data:
            numbers = voice_data.split()
            resultado = int(numbers[1])/int(numbers[4])
            engine_speak(f"O resultado da divisão é: {resultado}")
        else:
            numbers = voice_data.split()
            resultado = int(numbers[1])/int(numbers[3])
            engine_speak(f"O resultado da divisão é: {resultado}")
    if op == "*":
        numbers = voice_data.split()
        resultado = int(numbers[1]) * int(numbers[3])
        engine_speak(f"O resultado da multiplicação é: {resultado}")
    if op == "**":
        numbers = voice_data.split()
        resultado = int(numbers[1]) ** int(numbers[4])
        engine_speak(f"O resultado da potência é: {resultado}")