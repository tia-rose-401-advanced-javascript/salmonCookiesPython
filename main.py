# lowercase flask is the module I installed, uppercase Flask is the function will be executed in order to create the app object

from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
  return "Hello Tia"