from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():     #index関数の定義
    return render_template("index.html")

@app.route("/article1")
def article1():　#article1関数の定義　
    return render_template("article1.html")

@app.route("/article2")
def article2():　#article2関数の定義
    return render_template("article2.html")

if __name__ == '__main__':
    app.run(debug=True)