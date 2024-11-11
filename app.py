from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"]) # 通过 @，Flask 识别出 index() 函数应该在用户访问根路径时执行
def index():
    return(render_template("index.html"))

if __name__ == "__main__": # 第二次确认是main
    app.run()



