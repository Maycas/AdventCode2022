import sys, os, inspect
from typing import Callable
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list
import numpy as np

FILE_DIR = './data/warehouse.txt'


def create_stacks_from_input(file_directory:str) -> dict:
    lines = read_list(file_directory)

    STACK_POSITIONS = range(1, len(lines[0]), 4)

    # crawl through input lines
    crate_stacks = []
    for line in lines:
        level = []
        for position in STACK_POSITIONS:
            level.append(line[position])
        crate_stacks.append(level)
        
        # stop when reaching stack number 1 label 
        if level[0] == '1':
            break     
    
    # transpose current crates
    crate_stacks = np.array(crate_stacks).T.tolist()
    
    # reorder elements, remove whitespaces and convert into dictionary for easier manipulation
    crate_stacks = [stack[-1::-1] for stack in crate_stacks]
    crate_stacks = [
        [
            element for element in stack if not element.isspace()
        ]
        for stack in crate_stacks
    ]
    crate_stacks_dict = {stack[0]:stack[1:] for stack in crate_stacks}

    return crate_stacks_dict

def create_operations_moves_dict(file_directory: str) -> list[dict]:
    lines = read_list(file_directory)

    operations = []
    for line in lines:
        if line != '' and line[0] == 'm':
            line = line.split()
            operation = {
                'qty': int(line[1]),
                'from': int(line[3]),
                'to': int(line[-1])
            }
            operations.append(operation)

    return operations   

def operate_crane(stacks: dict, moves: list[dict]) -> dict:   
    for move in moves:
        qty = move['qty']
        crate_from = str(move['from'])
        crate_to = str(move['to'])
        
        for idx in range(qty):
            if len(stacks[crate_from]) > 0:
                crate_to_move = stacks[crate_from].pop()
                stacks[crate_to].append(crate_to_move)   
    return stacks

def top_elements_in_crates(file_directory: str) -> str:
    stacks = create_stacks_from_input(file_directory)
    moves = create_operations_moves_dict(file_directory)
    moved_stacks = operate_crane(stacks, moves)
    
    top_stacks = ''
    for top_stack in moved_stacks.values():
        top_stacks += top_stack[-1]
    
    return top_stacks


print(f"Part 1 - Top items in crates: {top_elements_in_crates(FILE_DIR)}")