# 홈페이지 작성, 디버깅 모드, 포트 5000번, 홈페이지는 화면에 Helloworld"만 출력
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "helloworld"

if __name__ == "__main__":
    # 웹 상의 기본 포트는: http => 80 => 기본 포트라서 입력 시 생략 가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, host='0.0.0.0', port=5000)