from bottle import get, run, request
import json

from crawler1 import parse_short_obj, parse_full_obj


@get('/short_news')
def return_short_news():
    count = request.params.get('count', 0)  # count =
    return json.dumps(parse_short_obj(count), ensure_ascii=False)


@get('/full_news')
def return_full_news():
    print(type(request.params.get('count')))
    count = request.params.get('count', [0])[0]  # count =
    return json.dumps(parse_full_obj(count), ensure_ascii=False)


if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
