import requests
import pandas as pd
import os

windows_user_name = os.path.expanduser('~')

# 데이터 처음 만들기
url = 'https://api.themoviedb.org/3/movie/popular?api_key=925b81e06374e04b7cdf9ac9b95b77a2&language=ko&region=kr&page=1'
data = requests.get(url).json()


df = pd.DataFrame(data['results'])

df_preprocessed = df[
    ['id', 'title', 'overview', 'release_date', 'original_title', 'poster_path', 'backdrop_path',
     'vote_average', 'vote_count', 'popularity', 'adult', 'genre_ids']]


result = df_preprocessed


# 돌면서 데이터 추가하기
for page in range(2, 201):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=925b81e06374e04b7cdf9ac9b95b77a2&language=ko&region=kr&page={page}'
    data = requests.get(url).json()

    df = pd.DataFrame(data['results'])
    df_preprocessed = df[
        ['id', 'title', 'overview', 'release_date', 'original_title', 'poster_path', 'backdrop_path',
         'vote_average', 'vote_count', 'popularity', 'adult', 'genre_ids']]

    result = pd.concat([result, df_preprocessed], ignore_index=True)
    print(result)

final = result.assign(view_cnt=0)
final.to_csv(f'{windows_user_name}/Desktop/data.csv', encoding="utf-8-sig")



