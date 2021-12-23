# coding = utf-8

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.34.1.132:27017/')
# localgost는 대표 ip주소, 컴퓨터 포트27017
db = client.data_db
# collection에 연결

@app.route("/")
def home():
    return render_template('index.html')

# API 데이터불러오기 테스트.
@app.route('/test', methods=['GET'])
def datatest_get():
   articles = list(db.toursdata.find({}, {'_id': False}))
   print(articles)
   return jsonify({'articles': articles})


# API POST 테스트
@app.route('/test', methods=['POST'])
def test_post():
   thema_receive = request.form['thema_give']

   doc = {
       'thema': thema_receive
   }
   db.themes.insert_one(doc)

   return jsonify({'result':'success', 'msg': '검색완료'})


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)





