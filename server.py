# fastapi: 파이썬 비동기 통신을 지원하는 라이브러리
from fastapi import FastAPI
# Cross-Origin Resource Sharing = CORS
from fastapi.middleware.cors import CORSMiddleware

from service.weather import get_weather

app = FastAPI()

# 아래의 host는 접근 가능하다.
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/index")
def index():
    return {"msg":"hello world"}

'''
dt_txt = data['list'][i]['dt_txt']
day_txt = dt_txt.split(' ')[i]
time_txt = dt_txt.split(' ')[i][:2]
temp = data['list'][i]['main']['temp']
temp_min = data['list'][i]['main']['temp_min']
temp_max = data['list'][i]['main']['temp_max']
humidity = data['list'][i]['main']['humidity']
wind_speed = data['list'][i]['wind']['speed']
feels_like = data['list'][i]['main']['feels_like']
pop = data['list'][i]['pop']
'''

@app.get("/api/wewh") # 이러한 url에 get method로 접근하면 아래 코드 실행
def wewh(search_addr):
    return get_weather(search_addr)