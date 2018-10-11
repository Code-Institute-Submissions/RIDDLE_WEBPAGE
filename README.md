# Milestone project - Riddle Game


#1. ***Design***
The frontend of my design is from BootStrap using there reponsive layout design and flexbox for displaying the content. I used Python for handling the backend of the webpage, handling POST and GET requests from forms and retrieving data from CSV files and JSON files when needed. 

#2. How the game works

Once your brought to the webpage you are prompted to enter a username and login. Your username is then stored in a txt file and you are directed to the main riddle page where you are shown a riddle to guess. Wrong guesses will result in loosing a point and your guess will be stored and displayed at the bottom of the page when you click on the button to see previous guesses. Right guesses will increment your score by one and move you onto the next riddle. You have a display for the lengh of riddles remaining just below the main riddle so you know how far you have to go to be scored for the leaderboard. If you have a riddle that you wish to share with others then you can add this to our collection for others to guess. A quicksort Algorithm is used to sort through the leaderboard CSV file and display them in a an acending order.

# 3. Software used
**1.** *VS Code / Cloud 9*  
VS code was the editior I chose to use. Plugins used where live server, markdown preview, python linting and python.

**2.** *Heroku for deployment*
Heroku was the website we had to use for deployment. Uploaded my code from github to cloud9 and installed requirements.txt and Procfile so heroku could read the file was python and the requirements needed.

**3.** *Python3 / HTML / CSS / Javascript*
Python3 - Version 3.6.5
HTML - Used both a base html file to be used across my templates and standard HTML layout for the templates that were not using base.html.
CSS - Used CSS for all my styling of the webpage.
Javascript - Very small amount of Javascript used for button operations.

**4.** *Flask*
Flask is a micro framework used for my webpage. 
From flask I imported the following - Flask, render_template, request, redirect, flash and url_for.
These help with url routing and templates being rendered once redirected by the webpage. Flash is used to display messages and request handles GET and POST requests from forms within my webpage.




    
