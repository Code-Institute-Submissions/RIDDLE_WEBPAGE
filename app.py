import os 
import json
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

def write_to_file(filename, data):
    """ handle process of writing to file """
    with open(filename, "a") as file:
        file.writelines(data)


# <------------ global variables ---------->

leaderboard_score = {}


# <-------------------- LOGIN PAGE ---------------------->
@app.route("/")
@app.route ("/", methods=["POST", "GET"])
def index():
    
    if request.method == "POST":
        username = request.form["username"]
        write_to_file("data/users.txt", username + "\n")
        leaderboard_score[username] = 0
         
         
         
        return render_template("riddle.html", username=username)
    return render_template("index.html")
    


# <---------------------- MAIN PAGE ------------------------->

@app.route('/<username>/riddle/', methods=["POST", "GET"])
def riddle():
    print(leaderboard_score)
    
    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)

  
    
    return render_template("riddle.html", data=data)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)