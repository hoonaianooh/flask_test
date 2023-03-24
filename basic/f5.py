'''
    - POST방식으로 데이터 전송하기
        - 클라이언트 (json, Xml, TEXT, Form(키=값&키=값), Form-encode,Graphql, Binary)
            - from 전송, 화면 껌벅 => 화면 전환, (Form, Form-encode 형식)
                <form action="http://127.0.0.1:5000/link" method="post">
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>                    
                    <input name="submit" value="전송"/>                    
                </form>
            - ajax 가능 (jQuery로 표현), 화면은 현재 화면 유지
                -(json, Xml, TEXT, Form(키=값&키=값...), Form-encode,Graphql, Binary) 방식가능
                $.get({
                    url:"http://127.0.0.1:5000/link",
                    data:"ame=hello&age=100",
                    success:( res )=>{},
                    error:(err)=>{}
                })
        - 서버
            - get 방식 데이터 추출
            - name = request.form.get('name')
            - age  = request.form.get('age')

    -/link 쪽으로 요청하는 방식은 다양할 수 있다. 단 사이트 설계 상 1가지로만 정의되어 있다면
     다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래칭, 해킹 등이 대상)
     이런 접근을 필터링할 것인가? 보안의 기본사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# @app.route() => 기본적으로 GET방식
# 메소드 추가는 => methods=['POST', ...]
@app.route('/login', methods=['POST', 'GET'])
def login():
    # method별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: # post
        # request.form['uid'] # 값이 누락되면 서버 셧다움되므로 왼쪽코드 사용금지
        # 1. 로그인 정보 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw') # 암호는 차후에 암호화해야 한다(관리자도 볼 수 없다, 해싱)
        print( uid, upw )
        # 2. 회원 여부 쿼리
        from d4 import select_login
        result = select_login(uid, upw)
        if result: # 3. 회원이면
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
            pass
        else:      # 4. 회원이 아니면
            # 4-1. 적당한 메시지 후 다시 로그인 유도
           return render_template('error.html') 
           pass
    #return redirect('https://www.naver.com') # 요청을 다른 URL로 포워딩한다


if __name__ == "__main__":
    app.run(debug=True)