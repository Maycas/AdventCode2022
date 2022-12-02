# Importing methods from utils
import os
import sys

sys.path.insert(1, os.path.abspath(".."))
from lib.utils import read_list

FILE_DIR = './strategy.txt'

PLAYER = 1
OPPONENT = 0

# The SYMBOLS have been encoded in a way that we are providing an order like: 
#     Rock (0) - Paper (1) - Scissors (3)
# This means that the player always beats the option on his left and loses against the 
# option on his right. So, if (player - opponent == 1), then the player wins Then, if the
# player selects scissors and opponent selects rock, then player the player loses 
# (player - opponent == 2)
# Finally, there's an edge case, where player selects rock and opponent selects 
# scissors, then player - opponent = -2. In that last case, we need to convert 
# this -2 using the modulo operator so it becomes a 1 and the player wins. 
# Eg: (player - opponent) % 3 = 1, and then the player wins.
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

# For the outcome symbols, we know the difference that needs to happen for an specific
# outcome to happen. We'll be using these to compute what should be the symbol we need
OUTCOME_SYMBOLS = {
    'X': {
        'name': 'lose',
        'difference': 2
    },
    'Y': {
        'name': 'draw',
        'difference': 0
    },
    'Z': {
        'name': 'win',
        'difference': 1
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
    player_score = 0
    opponent_score = 0
    difference = (SYMBOLS[player_symbol]['value'] - SYMBOLS[opponent_symbol]['value']) % 3

    if difference == 1:
        opponent_score = SCORES['lose']
        player_score = SCORES['win'] 
    elif difference == 2:
        opponent_score = SCORES['win']
        player_score = SCORES['lose']
    elif difference == 0:
        opponent_score = SCORES['draw']
        player_score = SCORES['draw']

    opponent_score += SCORES[SYMBOLS[opponent_symbol]['name']]
    player_score += SCORES[SYMBOLS[player_symbol]['name']]

    return opponent_score, player_score


def get_desired_outcome_symbol(opponent_symbol: str, player_symbol: str) -> list:    
    # Sub-setting symbols to collect only 'A', 'B', 'C'
    symbols = {key: value for key, value in SYMBOLS.items() if key in ['A', 'B', 'C'] }
    player_symbol_difference_value = (OUTCOME_SYMBOLS[player_symbol]['difference'] + SYMBOLS[opponent_symbol]['value']) % 3
    player_symbol_to_play = [key for key, value in symbols.items() if value['value'] == player_symbol_difference_value]
    return player_symbol_to_play[0]


def update_all_games(games: list):
    updated_game_outcomes_list = []
    for game in games:
        outcome = get_desired_outcome_symbol(game[OPPONENT], game[PLAYER])
        updated_game_outcomes_list.append([game[0], outcome])
    return updated_game_outcomes_list


def run_games(games: list) -> tuple:
    total_player_score = 0
    total_opponent_score = 0
    for game in games:
        opponent_score, player_score = score_calculation(game[OPPONENT], game[PLAYER])
        
        total_player_score += player_score
        total_opponent_score += opponent_score
    
    return total_opponent_score, total_player_score


def show_results(file_directory:str) -> None:
    games = format_game_input(file_directory)

    print("Part 1 - Without knowing the code the elf used for the strategy")
    opponent_score, player_score = run_games(games)
    print(f"The player would score: {player_score}")
    print(f"The opponent would score: {opponent_score}")

    print("\n##################\n")

    print("Part 2 - Knowing the strategy that needs to be followed")
    updated_games = update_all_games(games)
    opponent_score, player_score = run_games(updated_games)
    print(f"The player would score: {player_score}")
    print(f"The opponent would score: {opponent_score}")


show_results(FILE_DIR)


