from flask import Flask
from flask import render_template, request
import textblob, os
import google.generativeai as genai

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

@app.route("/genai_ask", methods = ["GET", "POST"])
def genai_ask():
    return(render_template("genai_ask.html"))

@app.route("/genai_result", methods = ["GET", "POST"])
def genai_result():
    api = os.getenv("maskersuite")
    # input: " [export maskersuite="your_api_key"] " in the terminal
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    q = request.form.get("q")
    response = model.generate_content(q)
    r = response.candidates[0].content.parts[0].text
    return(render_template("genai_result.html", r=r))

@app.route("/paynow", methods = ["GET", "POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__": # 第二次确认是main
    app.run()
