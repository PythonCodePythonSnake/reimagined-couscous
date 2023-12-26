from flask import Flask, request
from random import randint
from json import load, dump
import numpy as np

app = Flask(__name__)

@app.route("/new", methods=["GET", "POST"])
def new():
    def new_game_id():
        id = []
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for _ in range(20):
            id.append(alpha[randint(0, 25)])
        return "".join(id)
    
    with open("data.json") as file:
        existing = load(file)
    
    id = new_game_id()
    while id in existing.keys(): id = new_game_id()
    
    existing.update({id: {"players": request.json["players"], "board": np.full((10, 10), 0)}})
    
    with open("data.json") as file:
        dump(existing, file)
    
    return {"game_id": id}

@app.route("/board", methods=["GET", "POST"])
def board():
    return {"move": request.json.get("move")}
