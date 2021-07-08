# Flask web启动器的扩展

from flask import Flask

## 1、需要一个变量承载Flask的启动对象
web = Flask(__name__)

## 2、所有基于Flask启动对象的变量下的路由，均由@变量名.route（）绑定
@web.route('/perry')
def index():
    return 'Hello, Perry'

## 3、主函数，启动器
if __name__ == '__main__':
    web.run()