import requests # 보내고자 하는 ip로 전송하기 위해 라이브러리
import json # python data 형식을 json 형식으로 변환하기 위한 라이브러리

def get_weather(city_en_code):

    city = city_en_code
    apikey = "apikey"
    lang = "kr"

    api = f"""http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&lang={lang}&units=metric"""

    result = requests.get(api)
    data = json.loads(result.text)
    # print(data)

    # 총 40개의 데이터 존재 (3시간 간격의 5일치 데이터)
    dt_txt = data['list'][3]['dt_txt']
    temp = data['list'][3]['main']['temp']
    temp_min = data['list'][3]['main']['temp_min']
    temp_max = data['list'][3]['main']['temp_max']
    humidity = data['list'][3]['main']['humidity']
    wind_speed = data['list'][3]['wind']['speed']
    feels_like = data['list'][3]['main']['feels_like']
    pop = data['list'][3]['pop']

    day_txt = dt_txt.split(' ')[0]
    time_txt = dt_txt.split(' ')[1][:2]

    return {
        "day_txt":day_txt,
        "time_txt":time_txt,
        "temp":temp,
        "temp_min":temp_min,
        "temp_max":temp_max,
        "humidity":humidity,
        "wind_speed":wind_speed,
        "feels_like":feels_like,
        "rainfall":pop
    }


''' 출력 결과...
{
'cod': '200',
'message': 0,
'cnt': 40,
'list':
    [
    {
    'dt': 1702544400,
    'main':
        {'temp': 7.66, 'feels_like': 5.37, 'temp_min': 7.4, 'temp_max': 7.66, 'pressure': 1020, 'sea_level': 1020, 'grnd_level': 1013, 'humidity': 83, 'temp_kf': 0.26},
    'weather':
        [{'id': 500, 'main': 'Rain', 'description': '실 비', 'icon': '10n'}],
    'clouds': {'all': 100},
    'wind': {'speed': 3.54, 'deg': 77, 'gust': 10.49},
    'visibility': 7924, 'pop': 1,
    'rain': {'3h': 2.57},
    'sys': {'pod': 'n'},
    'dt_txt': '2023-12-14 09:00:00'}
    ... 이런 게 3시간 단위로 5일치 출력됩니다.
'''
