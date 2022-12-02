# Importing methods from utils
import os
import sys

sys.path.insert(1, os.path.abspath(".."))
from lib.utils import read_list

FILE_DIR = './strategy.txt'

PLAYER = 1
OPPONENT = 0

SYMBOLS = {
    'A': {
        'name': 'rock',
        'value': 0
    },
    'B': {
        'name': 'paper',
        'value': 1
    },
    'C': {
        'name': 'scissors',
        'value': 2
    },
    'X': {
        'name': 'rock',
        'value': 0
    },
    'Y': {
        'name': 'paper',
        'value': 1
    },
    'Z': {
        'name': 'scissors',
        'value': 2
    },
}

SCORES = {
    'win': 6,
    'draw': 3,
    'lose': 0,
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def format_game_input(file_directory: str) -> list:
    lines = read_list(file_directory)
    game_pairs = [game.split(' ') for game in lines] 
    return game_pairs

def score_calculation(opponent_symbol: str, player_symbol: str) -> int:  
    # Determining the winner
    # The SYMBOLS have been structured in a way that we are providing an order like: 
    #     Rock (0) - Paper (1) - Scissors (3)
    # This means that the player always beats the option on his left and loses against the 
    # option on his right. So, if (player - opponent == 1), then the player wins Then, if the
    # player selects scissors and opponent selects rock, then player the player loses 
    # (player - opponent == 2)
    # Finally, there's an edge case, where player selects rock and opponent selects scissors,
    # then player - opponent = -2. In that last case, we need to convert this -2 using 
    # the modulo operator so it becomes a 1 and the player wins. Eg: (player - opponent) % 3 = 1, and then the player wins.
    player_score = 0
    difference = (SYMBOLS[player_symbol]['value'] - SYMBOLS[opponent_symbol]['value']) % 3

    if difference == 1:
        player_score = SCORES['win'] 
    elif difference == 2:
        player_score = SCORES['lose']
    elif difference == 0:
        # Draw
        player_score = SCORES['draw']
        
    player_score += SCORES[SYMBOLS[player_symbol]['name']]

    return player_score


def run_games(file_directory:str) -> tuple:
    games = format_game_input(file_directory)

    total_player_score = 0
    for game in games:
        player_score = score_calculation(game[OPPONENT], game[PLAYER])
        total_player_score += player_score
    
    return total_player_score


score = run_games(FILE_DIR)
print(score)


