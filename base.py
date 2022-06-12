import json

from simhash import Simhash


class NewsChecker:
    def __init__(self):
        self._load_hash()

    def _load_hash(self):
        with open('hash.json') as f:
            data = json.load(f)
            self.hash = data['items']

    def check(self, text):
        news_hash = Simhash(text)

        news = []
        for item in self.hash:
            hash = Simhash(item['hash'])
            news.append((item['id'], news_hash.distance(hash)))
        return news
