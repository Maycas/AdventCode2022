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
    '''
    Reads a file inside the specified file_directory, containing the 
    rows of the game outcomes and formats them into a nested list
    with all the game pair outcomes

    Parameters
    ----------
    file_directory: str, mandatory
        The directory where the file to read the lines is 
        stored.

    Returns
    ----------
    game_pairs: list
        List for all to be played game symbols. Each position in the
        list has the pair of symbols for both the opponent and the
        player
    '''
    lines = read_list(file_directory)
    game_pairs = [game.split(' ') for game in lines] 
    return game_pairs


def score_calculation(opponent_symbol: str, player_symbol: str) -> int:
    '''
    Calculates the score of a single given pair of symbols for a Rock
    Paper Scissor game.
 
    Parameters
    ----------
    opponent_symbol: str, mandatory
        The symbol that the opponent will choose in the game.
        Accepted values: 'A', 'B', 'C'
    player_symbol: str, mandatory
        The symbol that the player will choose in the game.
        Part 1 accepted values: 'X', 'Y', 'Z'
        Part 2 accepted values: 'A', 'B', 'C'

    Returns
    ----------
    opponent_score, player_score: tuple
        Tuple with the score for the opponent and the player
        for each given game
    '''  
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
    '''
    Knowing which is the output the game should have (win, lose, draw), indicated by player_symbol
    'X', 'Y', 'Z', it returns the symbol the player needs to play in order to generate
    that outcome
 
    Parameters
    ----------
    opponent_symbol: str, mandatory
        The symbol that the opponent will choose in the game.
        Accepted values: 'A', 'B', 'C'
    player_symbol: str, mandatory
        The symbol that the player will choose in the game.
        Accepted values: 'X', 'Y', 'Z'

    Returns
    ----------
    player_symbol_to_play: str
        The symbol that needs to be played to generate the specified outcome
    '''     
    # Sub-setting symbols to collect only 'A', 'B', 'C'
    symbols = { key: value for key, value in SYMBOLS.items() if key in ['A', 'B', 'C'] }
    player_symbol_difference_value = (OUTCOME_SYMBOLS[player_symbol]['difference'] + SYMBOLS[opponent_symbol]['value']) % 3
    player_symbol_to_play = [key for key, value in symbols.items() if value['value'] == player_symbol_difference_value]
    return player_symbol_to_play[0]


def update_all_games(games: list):
    '''
    Updates the list of symbols for all games replacing 'X', 'Y', 'Z'
    for the symbol the player needs to play in order to generate the given
    outcome
 
    Parameters
    ----------
    games: list 
        List for all to be played game symbols. Each position in the
        list has the pair of symbols for both the opponent and the
        player. This list is the original one coming with the 
        'X', 'Y and 'Z' symbols for the player symbols

    Returns
    ----------
    updated_game_outcomes_list: list
        List with the values of 'X', 'Y' and 'Z' translated to the
        'A', 'B', 'C' symbols depending on the expected outcomes
    '''
    updated_game_outcomes_list = []
    for game in games:
        outcome = get_desired_outcome_symbol(game[OPPONENT], game[PLAYER])
        updated_game_outcomes_list.append([game[0], outcome])
    return updated_game_outcomes_list


def run_games(games: list) -> tuple:
    '''
    Runs all the game pairs in order to determine the final score 
    for the player and the opponent, after all games have run
 
    Parameters
    ----------
    games: list 
        List for all to be played game symbols. Each position in the
        list has the pair of symbols for both the opponent and the
        player.

    Returns
    ----------
    total_opponent_score, total_player_score: tuple
        A tuple with the opponent's score and the player's score
        at the end of all the games
    '''
    total_player_score = 0
    total_opponent_score = 0
    for game in games:
        opponent_score, player_score = score_calculation(game[OPPONENT], game[PLAYER])
        
        total_player_score += player_score
        total_opponent_score += opponent_score
    
    return total_opponent_score, total_player_score


def show_results(file_directory:str) -> None:
    '''
    Given a directory of a file containing rows of rock-paper-scissor games,
    returns the score results for both parts of the puzzle.

    Parameters
    ----------
    file_directory: str, mandatory
        The directory where the file to read the lines is 
        stored.
    '''
    games = format_game_input(file_directory)

    print("Part 1 - Without knowing the code the elf used for the strategy\n")
    opponent_score, player_score = run_games(games)
    print(f"The player would score: {player_score}")
    print(f"The opponent would score: {opponent_score}")

    print("\n##################\n")

    print("Part 2 - Knowing the strategy that needs to be followed\n")
    updated_games = update_all_games(games)
    opponent_score, player_score = run_games(updated_games)
    print(f"The player would score: {player_score}")
    print(f"The opponent would score: {opponent_score}")


show_results(FILE_DIR)


