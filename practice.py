# 0. import
import requests
from pprint import pprint

# 1. URL 및 요청변수 설정
# https://deverlopers.themoviedb.org/3/movies/get-now-playing
# http로 요청보낼거야, 주소가 있고 그 주소에 요청 파라미터에 값이 있어
# https://api.themoviedb.org/3/movie/now_playing?api_key=925b81e06374e04b7cdf9ac9b95b77a2&region=KR&language=ko
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
params = {
    'api_key' : '925b81e06374e04b7cdf9ac9b95b77a2',
    'region' : 'KR',
    'language' : 'ko'
}


# 2. 요청 보낸 결과 지정
response = requests.get(BASE_URL+path,params=params)
print(response.status_code, response.url)
data = response.json()                              # 객체 ==> 클래스 + 함수

print(type(response),type(data))                    # response, dict
print(data.keys())
print(type(data.get('results')))                    # list
print(data.get('results')[0])
# 3. 조작
