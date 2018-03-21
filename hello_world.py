# coding:utf-8

# 带入 Flask 类，这个类的实例是一个 WSGI 应用程序
from flask import Flask

"""第一个参数是应用模块或者包的名称，如果你使用单一的模块（如本例），你应该使用 
__name__ ，因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同
（ 也即是 '__main__' 或实际的导入名）。"""

app = Flask(__name__)


"""route 装饰器可以告诉我们什么样的 URL 可以触发函数,这个函数返回我们希望在网页
中看到的信息"""


@app.route('/')
def index():
    return "Index"


@app.route('/hello')
def hello_world():
    return "Hello world!"


@app.route('/user/<username>')
def user(username):
    return "User: %s" % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post: %d" % post_id


if __name__ == '__main__':
    app.run(debug=True)

"""外部可访问的服务器服务
app.run(host='0.0.0.0')"""

"""调试
调试模式是绝对不可以使用在生产环境中的。
1）
app.debug = True
app.run()
2）
app.run(debug=True)
"""
