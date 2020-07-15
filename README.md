# Codeacademy Counter Science Project : Coin Flip 1

## Goal

Build a console application that allows the user to guess the outcome of a random coin flip.  

## User Stories/Features as described by the challenge

Basic

User Story: As a user I want to be able to guess the outcome of a random coin flip(heads/tails).  
User Story: As a user I want to clearly see the result of the coin flip.  
User Story: As a user I want to clearly see whether or not I guessed correctly.  

Intermediate Challenge

User Story: As a user I want to clearly see the updated guess history (correct count/total count).  
User Story: As a user I want to be able to quit the game or go again after each cycle.  

Advanced Challenge

User Story: As a user I want to be able to guess the outcome of a 6-sided dice roll (1-6), with the same feature set as the coin flip (see above).


### Dependency Installation instructions
Can be installed via pipenv (pipenv install) in the directory containing the pipfile
OR  
pip install -r requirements.txt

### Features that the project implements
1. Choice between tossing a coin or rolling a die between each game
2. A random result from random.org api (atmospheric randomness) or python's random module   
if the connection can't be made
3. Display accuracy rate after each game
4. Connection Errors logged in an app.log file 

