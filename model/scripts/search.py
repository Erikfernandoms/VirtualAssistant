from model.scripts.engine_speak import engine_speak
import webbrowser

def search_google(voice_data):
    terms = voice_data.split()[1:]
    search_term = " ".join(terms)
    url = "http://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no google")

def search_youtube(voice_data):
    terms = voice_data.split()[1:-2]
    search_term = " ".join(terms)
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    engine_speak(f"Aqui está o que eu encontrei sobre: {search_term} no youtube")