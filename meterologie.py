import requests

api_key = '84986cafb189c092f9c226eb2e185579'
city =input("Veuillez entrer une ville : ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ar&appid={api_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    # Convertir la réponse JSON en dictionnaire Python
    weather_data = response.json()
    #print(weather_data,"\n")
    # Extraire certaines informations
    city_name = weather_data['name']
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    
    # Afficher les informations météorologiques
    print(f'Météo à {city_name}:')
    print(f'Température: {temperature}°C')
    print(f'Description: {weather_description}')
else:
    print(f'Erreur {response.status_code}: {response.text}')
    
    
    
