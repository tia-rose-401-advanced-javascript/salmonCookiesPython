# lowercase flask is the module I installed, uppercase Flask is the function will be executed in order to create the app object

from flask import Flask

# Importing variables from settings file
from settings import NAME
from settings import SECOND_NAME

app=Flask(__name__)

@app.route("/")
def hello():
  return f"Hello {NAME}"


@app.route("/test")
def dustin():
  return f"Hello {SECOND_NAME}"