# the programme displays current weather forecast for the location provided in the command line

import json, requests, sys, pprint

#poniżej kod do pobierania danych o lokalizacji z wiersza poleceń
# if len(sys.argv) <2:
#     print('Usage: weather_forecast.py location')
#     sys.exit()
# location = ' '.join(sys.argv[1:]) #łączy argumenty wiersza poleceń od indeksu 1 do końca - dla złożonych nazw lokalizacji, np. Mińsk Mazowiecki

#ustawiamy lokalizację na sztywno, bo interesuje nas tylko Warszawa
location= 'Warsaw'

url = '''http://api.openweathermap.org/data/2.5/forecast?q=''' + location + '''&units=metric&APPID=eb3e385e1f12b2ef91e58bcab67f2d29'''
response = requests.get(url)
response.raise_for_status()

w = json.loads(response.text)['list'] #response.text przechowuje dane tekstowe jako JSON, bierzemy tylko część 'list'

#pprint.pprint(w) # wyświetli nam całą część 'list'


for forecast_dict in w:
    print("Weather forecast for: " + forecast_dict['dt_txt'] + ': ' + forecast_dict['weather'][0]['description']
          + ', temp. max: ' + str(forecast_dict['main']['temp_max']) + ', temp. min: ' + str(forecast_dict['main']['temp_min']))



