from simhash import Simhash
import json

data = {'items': []}

with open('news.json') as f:
    items = json.load(f)
    for item in items['items']:
        hash = Simhash(item['full_text'])
        data['items'].append({
            'id': item['id'],
            # 'title': item['title'],
            'hash': hash.value
        })


with open('hash.json', 'w') as f:
    json.dump(data, f)
