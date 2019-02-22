import os 
import csv
import json
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("KEY")

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
        
        
# <---------- HANDLES FOR CORRECT / INCORRECT GUESSES / LEADERBOARD ---------->

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


def skip_question(username):
    """ skip next question """
    current_riddle[username] += 1

    if leaderboard_score[username] > 2:
        leaderboard_score[username] -= 2
    else:
        leaderboard_score[username] = 0

# <------------  DICTIONARY VARIABLES FOR GAME PLAY ---------->


leaderboard_score = {}
current_riddle = {}

# <-------------------- LOGIN PAGE ---------------------->


@app.route("/")
@app.route("/", methods=["POST", "GET"])
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
    guesses = display_guesses()

    if request.method == "POST":

        guess = request.form['guess']

        if guess.upper() == data[current_riddle[username]]["answer"].upper() and not 'next' in request.form:
            if length == current_riddle[username] + 1:
                write_to_file("data/leaderboard.csv", username + "," + str(leaderboard_score[username] +1) +  "\n")
                return redirect(url_for("endgame", username=username))
            else:
                correct_guess(username)

        elif 'next' in request.form:

            if length == current_riddle[username] + 1:
                write_to_file("data/leaderboard.csv", username + "," + str(leaderboard_score[username]) + "\n")
                return redirect(url_for("endgame", username=username))
            else:
                skip_question(username)

        else:
            incorrect_guess(username, guess)
            guesses = display_guesses()

    return render_template("riddle.html", username=username,
                           data=data,current=current_riddle[username],
                           riddle_length=length,
                           score=leaderboard_score[username],
                           guess=guesses)


# <-------------- ADDING YOUR OWN RIDDLES -------------->


@app.route('/addriddle/', methods=["POST", "GET"])
def add_riddle():
    riddles = []

    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)
        for lines in data:
            riddles.append(lines)

    if request.method == "POST":
        flash("Your riddle has been uploaded, thank you! ")
        riddle = {
            "id": riddles[-1]["id"] + 1,
            "riddle": request.form["form-question"].replace(",", ""),
            "answer": request.form["form-answer"].replace(",", ""),
        }

        riddles.append(riddle)

        with open("data/riddle.json", "w") as json_data:
            json.dump(riddles, json_data, indent=4)

    return render_template("add_riddle.html")


# <---------------- VIEW ALL RIDDLES ADDED --------------->

@app.route('/viewriddles/')
def view_riddles():
    riddles = []

    with open("data/riddle.json", "r") as json_data:
        data = json.load(json_data)
        for lines in data:
            riddles.append(lines)

    return render_template('view_riddles.html', riddles=riddles)

# <--------------- END OF GAME / LEADERBOARD -------------->


@app.route("/leaderboard")
def leaderboard():
    
    peoples_score = []
    
    with open("data/leaderboard.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)    
        
        for data in csv_reader:
            peoples_score.append(tuple(data))
            
    sorted_final_scores = (sorted(peoples_score, key=lambda people: int(people[1]), reverse=True))
    
    if len(peoples_score) == 0:
        sorted_final_scores = 0
        return render_template("leaderboard.html", score=sorted_final_scores)
    else:
        return render_template("leaderboard.html", score=sorted_final_scores)


@app.route("/<username>/riddle/endgame/")
def endgame(username):

    return render_template("endgame.html", username=username)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)