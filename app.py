from flask import Flask, redirect

app = Flask(__name__)

# 首页请求
@app.route('/')
def hello_world():
    return 'Hello World!'

# 带参数的get请求
@app.route('/user/<name>')
def user(name):
    return 'Hello {}!'.format(name)

# 重定向
@app.route('/redirect')
def nologin():
    return redirect("http://www.baidu.com")

# 主函数
if __name__ == '__main__':
    app.run()
