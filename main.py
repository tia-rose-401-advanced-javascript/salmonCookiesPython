# lowercase flask is the module I installed, uppercase Flask is the function will be executed in order to create the app object

from flask import Flask, render_template

# Importing variables from settings file
from settings import NAME
from settings import SECOND_NAME

app=Flask(__name__)

@app.route("/")
def hello():
  # return f"Hello {NAME}"
  f"NAME: {NAME}"
  f"SECOND_NAME: {SECOND_NAME}"
  return render_template("home.html", name=NAME)
  # return render_template("hello.html", second_name=SECOND_NAME)


@app.route("/sales")
def dustin():
  f"SECOND_NAME: {SECOND_NAME}"
  return render_template("sales.html", second_name=SECOND_NAME)

  temple = env.get_template('home.html')
  output = template.render(title="Salmon Cookies")
  print (output)