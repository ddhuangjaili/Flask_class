from flask import Flask, redirect,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# 首页请求
@app.route('/')
def hello_world():
    # return 'Hello World!'
    current_time = datetime.utcnow()
    return render_template('index.html', current_time=current_time)

# 带参数的get请求
@app.route('/user/<name>')
def user(name):
    # return 'Hello {}!'.format(name)
    return render_template('user.html', name=name)

# 重定向
@app.route('/redirect')
def nologin():
    return redirect("http://www.baidu.com")


# 错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 主函数
if __name__ == '__main__':
    app.run()
