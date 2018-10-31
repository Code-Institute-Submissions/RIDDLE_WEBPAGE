## Riddle Game Milestone Project

#Riddle Game 


[Play the Riddle Game]( https://riddle-game-milestone-project.herokuapp.com/)

The Riddle Game webpage was created for a fun way of trying to guess riddles and have been created by others. Each correct guess you will be awarded with 1 point and any incorrect guesses you will be deducted 1 point.
Previous guesses are displayed in a drop down section for help. Once all riddles have been correctly guessed your name and score will be uploaded to a leaderboard.
If you can think of any riddles that other people would enjoy you can simply add them to the webpage by clicking on the link in the navbar and fill out the form provided.

 
## Website Functionality

Riddle game is a fun game where you can try and guess a riddle that is displayed on the screen.

How does the Riddle game work : 

 1. Login to the webpage throught the login screen.
 2. Once logged in you are brought the the main webpage. A single riddle is displayed in a box with an input bar undearneath for your guesses.
 3. Any correct guesses you are awarded with 1 point and any incorrect guesses you loose 1 point. Your score is displayed next to your name thoroughout.
 4. Once all riddles have been correctly guesses your score is unloaded to the leaderboard.
 5. Any riddles that you would like to add can be done by clicking on the link in the navbar and fill out the form provided.


## Technologies Used

- [Cloud9](https://c9.io/login)
    - **Cloud9** was the chosen IDE (integrated development environment) which is an online program based program. Can be easily accessed from any machine with a login and password. 

- [Python](https://www.python.org/)
    -  **Python**  was the chosen language used to write Little Recipes webpage. Python is a powerful programming language with many builtin functions and extensions. 

- [Bootstrap](http://getbootstrap.com/)
    - The project uses **Bootstrap**, a modern responsive front end framework. Bootstrap has excellent an excellent and easy to use grid system for making a responsive webpage if your in a mobile view to a large screen or tablet.

- [Heroku](https://id.heroku.com/login)
    -  **Heroku** is used for my webpage deployment. My code is committed to Heroku and add a requirements text file and procfile so Heroku knows which software has to be installed and what program my code is running.

## Testing Riddle game

1. Google Chrome - HTML / Javascript / Jquery / CSS where all tested through the google chrome developer tool. Error message would appear in the console if anything was detected. Errors where displayed with a file location and which line the fault was on. Google chrome developer tools has a responsive section in which my webpage could be tested on many different screen sizes to make sure everything was working correctly for any users screen. 

2. Flask  - Jinja has a built in debug tool. Any Python code that isn't formatted correctly or a response that is being processed to the backend an error message is displayed and the webpage is stopped at the current point the code is broken.

3. Webpage scenario testing was carried out on the login page, register page, recipe adding and search fields making sure the user was alerted if an input had been left blank or incorrectly filled in.


## Deployment

My webpage is deployed through Heroku. I created a Heroku app to which I created a Github repository thorough the command line. i added a requirements text file and a Procfile so Heroku knows what to install and what program my code is running. Once created I added all my code to Heroku and committed my work ready to be pushed to the Heroku branch. 