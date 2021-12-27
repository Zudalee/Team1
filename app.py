# coding = utf-8

<<<<<<< HEAD
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@3.34.1.132:27017/')  #localgost는 대표 ip주소, 컴퓨터 포트27017
db = client.data_db  #DB에 연결

@app.route("/")
def home():
    return render_template('index.html')

# DB 데이터 불러오는 API
@app.route('/datadb', methods=['GET'])
def datatest():

   thema_receive = request.args.get('thema_give') #thema_give를 요청하면 thema_receive로 받음
   print(thema_receive)
   tours = list(db.toursdata.find({'thema' : thema_receive}, {'_id': False})) #DB안에서 thema 값이 thema_receive인 데이터를 찾음
   return jsonify({'all_tours': tours}) #return한 값을 all_tours에 저장


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





=======
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('04.html')


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 35b2c3f84c64c546c51bdd71d4ac009f93015235
