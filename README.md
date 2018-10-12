# Milestone project - Riddle Game


### 1. Design
The frontend of my design is from BootStrap using there reponsive layout design and flexbox for displaying the content. I used Python for handling the backend of the webpage, handling POST and GET requests from forms and retrieving data from CSV files and JSON files when needed. 

### 2. How the game works

Once your webpage has loaded you are prompted to enter a username for logging in. Your username is then stored in a txt file and you are directed to the main riddle page where you are shown a riddle to guess. Wrong guesses will result in 1 point being deducted from your score and your guess will be stored and displayed at the bottom of the page when you click on the button to see previous guesses. Right guesses will increment your score by 1 and move you onto the next riddle. You have a display for the lengh of riddles remaining just below the main riddle so you know how far you have to go to be scored for the leaderboard. If you have a riddle that you wish to share with others then you can add this to our collection for others to guess. A quicksort Algorithm is used to sort through the leaderboard CSV file and display them in a an acending order.

### 3. Software used

**1.** *Cloud 9*  
Cloud 9 is IDE for writing, running, and debugging code.

**2.** *Heroku for deployment*
Heroku was used for deployment. Uploaded my code from cloud9, installed requirements.txt and Procfile so heroku could read the file was python and the requirements needed.

**3.** *Python3 / HTML / CSS / Javascript*
Python3 - Version 3.6.5
HTML - Used both a base html file to be used across my templates and standard HTML layout for the templates that were not using base.html.
CSS - Used CSS for all my styling of the webpage.
Javascript - Very small amount of Javascript used for button operations.

**4.** *Flask*
Flask is a micro framework used for my webpage. 
From flask I imported the following - Flask, render_template, request, redirect, flash and url_for.
These help with url routing and templates being rendered once redirected by the webpage. Flash is used to display messages and request handles GET and POST requests from forms within my webpage.

### 4. Testing
Chrome developer tools was used for testing, if there was anything wrong with my html, css or javascript files I would be alerted quickly. 
Another powerful test tool is flasks jinja error page that appeared when errors where detected, quickly by either stopping my webpage from loading in the browser or not loading a render_template request.

### 5. Play the riddle game 

**Play the game below by clicking link**
[Play game!!]
(https://riddle-game-milestone-project.herokuapp.com/)




    
