from flask import Flask, request
from random import randint
from json import load, dump

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
        existing = dict(load(file))
    
    id = new_game_id()
    while id in existing.keys(): id = new_game_id()
    existing[id] = {"players": request.json["players"], "board": f"{[[0 for _ in range(10)] for _ in range(10)]}"} #request.json["players"]
    print(existing)
    with open("data.json", "w") as file:
        dump(existing, file)
    return dict({"game_id" : id})

@app.route("/board", methods=["GET", "POST"])
def board():
    return {"move": request.json.get("move")}

@app.route("/exit", methods=["GET", "POST"])
def exit():
    try:
        with open("data.json") as file:
            existing = dict(load(file))
        del existing[request.json["game_id"]] #request.json["game_id"]
        with open("data.json", "w") as file:
            dump(existing, file)
        return {"success": "true"}
    except: return {"success": "false"}
