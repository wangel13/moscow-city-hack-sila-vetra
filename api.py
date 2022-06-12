from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS

from base import NewsChecker


base = Blueprint('api', __name__)


@base.route('/check', methods=('POST',))
def check():
    data = request.json
    text = data.get('text')
    k = int(data.get('k'))
    checker = NewsChecker()
    news = checker.check(text, k)
    news.sort(key=lambda x: x[1])
    news = news[:5]
    result = []
    for item in news:
        item_id = item[0]
        result.append({
            'id': item_id,
            'link': f'https://www.mos.ru/news/item/{item_id}/',
            'distance': item[1]
        })

    return jsonify({'news': result})


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.update(SECRET_KEY='123456')

    app.register_blueprint(base)
    return app


app = create_app()
