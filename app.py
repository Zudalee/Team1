# coding = utf-8

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'list 연결되었습니다!'})




