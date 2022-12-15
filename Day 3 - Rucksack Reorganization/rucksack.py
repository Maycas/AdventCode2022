# Importing methods from utils
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

FILE_DIR = './rucksacks.txt'

# read the rucksacks lines and split compartments
def format_input(file_directory: str) -> list[list[str]]:
    rucksacks = read_list(file_directory)

    formatted_list = []
    for rucksack in rucksacks:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        formatted_list.append([first_compartment, second_compartment])

    return formatted_list


# find common items in each compartment
def find_common_items(rucksack: list[list[str]]) -> list[str]:
    common_items = []
    first_compartment = rucksack[0]
    second_compartment = rucksack[1]

    for item in first_compartment:
        # if the item is in the compartment and hasn't been added already
        if (item in second_compartment) and (item not in common_items):
            common_items.append(item)
    return common_items


# generate priority dictionary
def generate_prio_dict() -> dict:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = alphabet + alphabet.upper()
    priorities = [num for num in range(1, 53)]

    return { letters[idx]: priorities[idx] for idx in range(len(letters)) }

# assign priorities
def assign_priorities(common_items: list, priorities: dict):
    priority_value = 0
    for item in common_items:
        priority_value += priorities[item]
    return priority_value
    

# run algorithm
def calculate_priority_sum(file_directory):
    priorities = generate_prio_dict()
    rucksacks = format_input(file_directory)
    sum_priority = 0

    for rucksack in rucksacks:
        common_items = find_common_items(rucksack)
        sum_priority += assign_priorities(common_items, priorities)

    return sum_priority


print(calculate_priority_sum(FILE_DIR))