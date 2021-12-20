import requests
from urllib import parse

url = "http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnWthrIdx"
api_key_utf8 = "gUumAEbmHnjp9J33lIoCsYEhgwBdCiXmhoz%2BM27dYl6D1iVm9SKQfqmxXA3E7U0TtQ0QnqCj1MYikJfNwzwopQ%3D%3D"
api_key_decode = parse.unquote(api_key_utf8)

params = {
    "Servicekey": api_key_decode,
    "pageNo": 1,
    "numOfRows": 10,
    "COURSE_ID": 1
    "CURRENT_DATE": 2021121810,
    "HOUR": 1

}
response = requests.get(url, params=params)

print(response.text)
