import requests
import json
from datetime import date
import urllib.parse
from model.scripts.engine_speak import engine_speak

accuweatherAPIKey = "cvm7SWOH3JaCUEc7EaGNbrPekez7H5yL"
mapBoxToken = 'pk.eyJ1IjoibHVpenRpbWJvIiwiYSI6ImNrcG4wbmY4MTI2NDIyeG13amloYjM0cHMifQ.dvbhlq4Tns9HzRp27qJ21A'
dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira',
               'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']


def get_coords():
    data = requests.get('http://www.geoplugin.net/json.gp')

    if data.status_code != 200:
        engine_speak('Não foi possível obter as informações da sua localização!')
        return None

    else:
        try:
            localizacao = json.loads(data.text)
            coordenadas = {}
            coordenadas['lat'] = localizacao["geoplugin_latitude"]
            coordenadas['long'] = localizacao["geoplugin_longitude"]

            return coordenadas

        except:
            return None


def get_local_code(lat, long):
    LocationAPIURL = "http://dataservice.accuweather.com/locations/v1/cities/" \
        + "geoposition/search?apikey=" + accuweatherAPIKey \
        + "&q=" + lat + "%2C" + long + "&language=pt-br"

    r = requests.get(LocationAPIURL)
    if r.status_code != 200:
        engine_speak("Não foi possível obter o código do local!")
        return None

    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse["LocalizedName"] + ", " \
                + locationResponse["AdministrativeArea"]["LocalizedName"] + ". " \
                + locationResponse["Country"]["LocalizedName"]
            infoLocal['codigoLocal'] = locationResponse["Key"]

            return infoLocal

        except:
            return None


def pegarTempoAgora(codigoLocal, nomeLocal):
    currentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
        + codigoLocal + "?apikey=" + accuweatherAPIKey \
        + "&language=pt-br"

    r = requests.get(currentConditionsAPIUrl)
    if r.status_code != 200:
        engine_speak("Não foi possível obter o clima atual!")
        return None

    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = CurrentConditionsResponse[0]["WeatherText"]
            infoClima['temperatura'] = CurrentConditionsResponse[0]["Temperature"]["Metric"]["Value"]
            infoClima['nomeLocal'] = nomeLocal

            return infoClima

        except:
            return None


def get5days_weather(codigoLocal):
    dailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
        + codigoLocal + "?apikey=" + accuweatherAPIKey \
        + "&language=pt-br&metric=true"

    r = requests.get(dailyAPIUrl)
    if r.status_code != 200:
        engine_speak("Não foi possível obter o clima atual!")
        return None

    else:
        try:
            DailyResponse = json.loads(r.text)
            infoClima5Dias = []

            for dia in DailyResponse['DailyForecasts']:
                climaDia = {}
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                diaSemana = int(date.fromtimestamp(
                    dia['EpochDate']).strftime('%w'))
                climaDia['dia'] = dias_semana[diaSemana]
                infoClima5Dias.append(climaDia)

            return infoClima5Dias

        except:
            return None


def mostrarPrevisao(lat, long):
    try:
        local = get_local_code(lat, long)
        climaAtual = pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])
        engine_speak("Previsão em: "  + climaAtual['nomeLocal'])
        engine_speak("Clima atual: " + climaAtual['textoClima'])
        engine_speak("Temperatura: " + str(int(climaAtual['temperatura'])) + "\xb0" + "C")

    except:
        engine_speak('Erro ao obter o clima atual!')


def search_local(local):
    _local = urllib.parse.quote(local)
    mapBoxGeocodeUrl = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' \
        + _local + '.json?access_token=' + mapBoxToken

    r = requests.get(mapBoxGeocodeUrl)
    if r.status_code != 200:
        engine_speak("Não foi possível obter a localização!")
        return None

    else:
        try:
            MapboxResponse = json.loads(r.text)
            coordenadas = {}
            coordenadas['long'] = str(
                MapboxResponse['features'][0]['geometry']['coordinates'][0])
            coordenadas['lat'] = str(
                MapboxResponse['features'][0]['geometry']['coordinates'][1])

            return coordenadas

        except:
            engine_speak('Erro ao obter os dados da localização!')

def get_weather(local):
    coordenadas = search_local(local)
    mostrarPrevisao(coordenadas['lat'], coordenadas['long'])
    

