from flask import Flask
from flask import render_template
import requests

raw_data = requests.get("https://api.npoint.io/f3048202801a77a36da6")
new_data = raw_data.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data=new_data)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:num>")
def post(num):
    if num == 1:
        blog = new_data[0]
    elif num == 2:
        blog = new_data[1]
    else:
        blog = new_data[2]

    return render_template("post.html", data=blog, num=num)


if __name__ == "__main__":
    app.run(debug=True)

