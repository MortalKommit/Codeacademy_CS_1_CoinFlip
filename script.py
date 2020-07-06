import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import Retry
import random
import logging

DEFAULT_TIMEOUT = 5 # seconds

# HTTP Timeout sub class for handling multiple timeouts
class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


#logging object configuration (root logger)
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

#modify requests retry policy
retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
http = requests.Session()
http.mount("https://", TimeoutHTTPAdapter(max_retries=retries))

def toss_coin():
    payload = {'num': 1, 'min':0, 'max': 1, 'col':1, 'base':10, 'format':'plain', 'rnd':'new'}
    response = None
    try:
        response = requests.get('https://random.org/integers', params = payload)
        errored = False
    except requests.exceptions.RequestException as e:
        logging.error(f'Request Exception (Connection Error)\nDetails:{e.__context__}')
        errored = True
    if getattr(response, 'status_code', None) == '200' and not errored:
        return int(response.text.split('\n')[0])
    
    return random.randint(0,1)
    
def roll_die():
    payload = {'num': 1, 'min':0, 'max': 5, 'col':1, 'base':10, 'format':'plain', 'rnd':'new'}
    response = None
    try:
        response = requests.get('https://random.org/integers', params = payload)
        errored = False
    except requests.exceptions.RequestException as e:
        logging.error(f'Request Exception (Connection Error)\nDetails:{e.__context__}')
        errored = True
    if getattr(response, 'status_code', None) == '200' and not errored:
        return int(response.text.split('\n')[0])
    return random.randint(0,5)
def play_coin_game():
    guess = input('Choose ([H]eads/[T]ails):')
    while guess.upper() not in ('H', 'T'):
        print('Invalid choice, enter H for Heads, T for Tails')
        guess = input('Choose ([H]eads/[T]ails):')
    
    guess = "Heads" if guess == "H" else "Tails"
    print(f'Your guess:{guess}')
    return guess

def play_dice_game():
    try:
        guess = int(input('Choose a number (1-6):'))
        while guess not in range(1,7):
            print('Invalid choice, guess must be a number between 1 - 6')
    except ValueError:
        print('Error! Must enter a number!')
    print(f'Your guess:{guess}')
    return int(guess)
def play_guess_game():
    successful_guesses = 0
    total_guesses = 0
    replay = True
    possible_outcomes = {'cointoss':('Heads', 'Tails'), 'diceroll':tuple(i for i in range(1,7))}

    while replay:
        game_choice = input('Choose a game to play ([C]oin Toss/[D]ice Roll):')
        while game_choice.upper() not in ('C','D'):
            print('Invalid game choice, enter C for Coin Toss, D for Dice Roll')
            game_choice = input('Choose a game to play ([C]oin Toss/[D]ice Roll):')
        if game_choice.upper() == 'C':
            game = 'cointoss'
            outcome = toss_coin()
            guess = play_coin_game()
        else:
            game = 'diceroll'
            outcome = roll_die()
            guess = play_dice_game()
        total_guesses += 1
        print(f'Result:{possible_outcomes[game][outcome]}')
        if possible_outcomes[game][outcome] == guess:
            successful_guesses += 1
            print("You guessed correctly!")
        else:
            print("Sorry!")
        print(f"Guess Accuracy:{successful_guesses}/{total_guesses}")
        replay = True if input("Play Again? (y/n):").upper() == 'Y' else False
        
    
play_guess_game()