import requests
import pandas as pd
import os

windows_user_name = os.path.expanduser('~')

# 데이터 처음 만들기
url = 'https://api.themoviedb.org/3/movie/popular?api_key=925b81e06374e04b7cdf9ac9b95b77a2&language=ko&region=kr&page=101'
data = requests.get(url).json()


df = pd.DataFrame(data['results'])
df_preprocessed = df[
    ['genre_ids', 'id']]

result = df_preprocessed

# 돌면서 데이터 추가하기
n = 3 #페이지 수
for page in range(1, n+1):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=925b81e06374e04b7cdf9ac9b95b77a2&language=ko&region=kr&page={page}'
    data = requests.get(url).json()

    df = pd.DataFrame(data['results'])
    df_preprocessed = df[
        ['genre_ids', 'id']]

    result = pd.concat([result, df_preprocessed], ignore_index=True)
    print(page)


df = pd.DataFrame()

# result.rename(columns={'id':'movie_id'})

id = 0
for i in range(0, len(result)):
    for genre in result.iat[i,0]:
        df = df.append({'movie_id':int(result.iat[i,1]), 'genre_id':int(genre)} , ignore_index=True)
        id += 1

print(df)




df.to_csv(f'{windows_user_name}/Desktop/movie_genre.csv', encoding="utf-8-sig")



