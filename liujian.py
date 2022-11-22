from werkzeug.serving import make_server

import settings
from flask import Flask , render_template , request , json

app = Flask(__name__)
app.config.from_object(settings)

users = []
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/<int:n1>/<int:n2>')
def add(n1 , n2):
    if n1 > 0 and n2 > 0:
        r = n1 + n2
        return '运算结果是：' + str(r)
    return '两个数必须大于零'


@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            user = {'username':username,'password':password}
            users.append(user)
            return '用户注册成功 <a href = "/">返回首页</a>'
        else:
            return '两次密码输入不一致'

        return '注册成功'
    return render_template('register.html')


@app.route('/show')
def show():
    r = json.dumps(users)
    return r




if __name__ == '__main__':
    # server = make_server('0.0.0.0', 7652, app)
    # server.serve_forever()
    app.run(port=7652, host='0.0.0.0') #(port=7652, host='0.0.0.0')
