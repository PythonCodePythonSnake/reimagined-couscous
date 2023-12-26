from flask import Flask, request
import random
#from json import loads, dump

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return {"move": request.json.get("move")}
