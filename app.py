from flask import Flask
from flask import render_template, request
import textblob

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"]) # 通过 @，Flask 识别出 index() 函数应该在用户访问根路径时执行
def index():
    return(render_template("index.html"))

@app.route("/main", methods = ["GET", "POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA", methods = ["GET", "POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result", methods = ["GET", "POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html", r=r))

if __name__ == "__main__": # 第二次确认是main
    app.run()

