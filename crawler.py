import requests
import json
import time
from bs4 import BeautifulSoup

all_items = {'items': []}

for page in range(1, 208, 1):
    print(page)
    response = requests.get(f'https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/articles?fields=id,title,full_text&from=2021-01-01+00:00:00&sort=-date&to=2022-06-12+23:59:59&per-page=50&page={page}')
    items = response.json()
    for item in items['items']:
        parsed = BeautifulSoup(item['full_text'], features="html.parser")
        item['full_text'] = parsed.get_text()
    all_items['items'].extend(items['items'])
    time.sleep(2)


with open('news.json', 'w') as f:
    json.dump(all_items, f)
