import requests, mysql.connector, sys, json, datetime
from mysql.connector import Error

if len(sys.argv) >= 2:
    city = (' '.join(sys.argv[1:]),)
else:
    city = (input('For which city would you like the weather? '),)
cityIdQuery = "SELECT CityID FROM DEVOPS.WeatherCityIDs WHERE CityName = %s"
apiKeyQuery = "SELECT APIKey FROM DEVOPS.APIMaster WHERE Website = 'OpenWeatherMap'"
with open('connection.json') as json_file:
    conParams = json.load(json_file)
try:
    con = mysql.connector.connect(host=conParams['host'], database=conParams['database'], user=conParams['user'], password=conParams['password'])
    if con.is_connected():
        print('Connected to DB.')
    cityCursor = con.cursor()
    cityCursor.execute(cityIdQuery, city)
    cityId = cityCursor.fetchall()[0][0]
    cityCursor.close()
    apiCursor = con.cursor()
    apiCursor.execute(apiKeyQuery)
    
    
    apiKey = apiCursor.fetchall()[0][0]
    

except Error as e:
    print('Could not connect to DB.', e)

def convertFromK(kTemp):
    degreesF = ((((kTemp - 273.15) * 9) / 5) + 32)
    return degreesF
forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?id={0}&appid={1}'.format(cityId, apiKey))
forecast.raise_for_status()

forecastJson = json.loads(forecast.text)

print('Sunset: {0}'.format(datetime.datetime.utcfromtimestamp(forecastJson['city']['sunset']+forecastJson['city']['timezone'])))

for cast in forecastJson['list']:
    print('Time: {0}'.format(datetime.datetime.utcfromtimestamp(cast['dt'] + forecastJson['city']['timezone'])))
    print('Temp: {0:.4g} degrees'.format(convertFromK(cast['main']['temp'])))
    if 'rain' in cast:
        if '3h' in cast['rain']:
            print('Rain(mm)): {0}'.format(cast['rain']['3h']))
    print('Humidity: {0}'.format(cast['main']['humidity']))
    print('Condition: {0}\n'.format(cast['weather'][0]['description']))
    