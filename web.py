from flask import Flask, request
import random
#from json import loads, dump

app = Flask(__name__)

@app.route("/board")
def board():
    return random.randint(1, 8)

app.run(debug=True)