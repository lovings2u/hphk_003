from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    p
    return "<ㅓㅗHello World"