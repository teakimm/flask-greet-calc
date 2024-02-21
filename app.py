from flask import Flask

app = Flask(__name__)
#TODO: add docstrings
@app.get("/welcome")
def welcome():
    return "welcome"

@app.get("/welcome/home")
def welcome_home():
    return "welcome home"

@app.get("/welcome/back")
def welcome_back():
    return "welcome back"
