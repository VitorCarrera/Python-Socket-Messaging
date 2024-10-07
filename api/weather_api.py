import requests

API_KEY = 'd1cfe2c9049322cc65b53fdf195fd39d'

def obter_temperatura():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Belém&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']

            return f'A temperatura atual em Belém é {temperature}ºC.'
        else:
            return "Não consegui obter a temperatuera no momento."
    except:
        return "Ocorreu um erro ao acessar a API: {e}"