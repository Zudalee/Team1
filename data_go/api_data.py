import requests, xmltodict, json

url = "http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnVilageFcst?serviceKey=gUumAEbmHnjp9J33lIoCsYEhgwBdCiXmhoz%2BM27dYl6D1iVm9SKQfqmxXA3E7U0TtQ0QnqCj1MYikJfNwzwopQ%3D%3D&pageNo=1&numOfRows=100&dataType=XML&CURRENT_DATE=2021121810&HOUR=12&COURSE_ID=1"
params = {'courseId':'1'}

content = requests.get(url, params=params).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body'], ensure_ascii=False)
jsonobj = json.loads(jsonString)

for item in jsonobj['items']['item']:

    print(item)




