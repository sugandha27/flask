from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, Welcome!"

@app.route("/d")
def d():
    return "Keep up the good work!"

@app.route("/<string:name>")
def hello(name):
    return f"Hello,{name}"