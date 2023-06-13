import requests

API_KEY = '21d6fd7162dfa118e90e157119d18887'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

city = input('Enter the city: ')
request_url = f'{BASE_URL}q={city}&units=imperial&APPID={API_KEY}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    degrees = round(((temp-32)*5)/9) # [(°F-32)×5]/9
    print('Weather condition: ',weather,)
    print('Temperature: ',degrees,'°C')  
else:
    print('Data not available.!!!') 


