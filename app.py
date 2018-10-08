import os 
import csv
import json
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

# <------------- FILE HANDLER --------------->

def write_to_file(filename, data):
    """ handle process of writing to file """
    with open(filename, "a") as file:
        file.writelines(data)

# <---------------GUESSES HANDLING ----------->

def display_guesses():
    guesses = []
    with open("data/new_guesses.csv", "r") as guess_data:
        all_guesses = csv.reader(guess_data)
        for lines in all_guesses:
            guesses.append(lines)
    
    return guesses
    
def add_guesses(username, request):
    """ writes guesses to csv file"""
    
    guess = (username, request)

    with open("data/new_guesses.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(guess)
        
        
# <---------- HANDLES FOR CORRECT AND INCORRECT GUESSES ---------->

def correct_guess(username):
    
    current_riddle[username] += 1
    leaderboard_score[username] += 1

def incorrect_guess(username, guess):
    """ writes guesses to csv file"""
    
    guess = (username, guess)
    
    with open("data/new_guesses.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(guess)
        
    if leaderboard_score[username] > 0:
        leaderboard_score[username] -= 1


# <------------  DICTIONARY VARIABLES FOR GAME PLAY ---------->

leaderboard_score = {}
current_riddle = {}

# <-------------------- LOGIN PAGE ---------------------->
@app.route("/")
@app.route ("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        write_to_file("data/users.txt", username + "\n")
        leaderboard_score[username] = 0
        current_riddle[username] = 0
         
        return redirect(url_for("riddle", username=username))
        
    return render_template("index.html")
    


# <---------------------- MAIN PAGE ------------------------->

@app.route("/<username>/riddle/", methods=["POST", "GET"])
def riddle(username):
    
    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)
        
    length = len(data)
    guess = display_guesses()

    if request.method == "POST":
        guess = request.form["guess"]
        
        if guess.upper() == data[current_riddle[username]]["answer"].upper():
            correct_guess(username)
        else:
            incorrect_guess(username, guess)
        
    
    return render_template("riddle.html", username=username,data=data,current=current_riddle[username], riddle_length=length, score=leaderboard_score[username], guess=guess)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)