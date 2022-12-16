# Importing methods from utils
import sys, os, inspect
from typing import Callable
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

FILE_DIR = './data/rucksacks.txt'


def split_rucksacks_compartments(file_directory: str) -> list[list[str]]:
    rucksacks = read_list(file_directory)

    formatted_list = []
    for rucksack in rucksacks:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        formatted_list.append([first_compartment, second_compartment])

    return formatted_list


def find_common_items_per_rucksack(rucksack: list[list[str]]) -> list[str]:
    common_items = []
    first_compartment = rucksack[0]
    second_compartment = rucksack[1]

    for item in first_compartment:
        # if the item is in the compartment and hasn't been added already
        if (item in second_compartment) and (item not in common_items):
            common_items.append(item)
    return common_items


def generate_prio_dict() -> dict:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = alphabet + alphabet.upper()
    priorities = [num for num in range(1, 53)]

    return { letters[idx]: priorities[idx] for idx in range(len(letters)) }


def assign_priorities(common_items: list, priorities: dict) :
    priority_value = 0
    for item in common_items:
        priority_value += priorities[item]
    return priority_value


# def calculate_rucksack_sum_priority(file_directory: str, priorities_dict: dict) -> int:
#     rucksacks = split_rucksacks_compartments(file_directory)
#     sum_priorities = 0

#     for rucksack in rucksacks:
#         common_items = find_common_items_per_rucksack(rucksack)
#         sum_priorities += assign_priorities(common_items, priorities_dict)

#     return sum_priorities


def priorities_aggregation(file_directory: str, priorities_dict: dict, splitting_function: Callable[[str] ,list[list[str]]], common_matching_function: Callable[[list[list[str]]], list[str]], aggregation_function: Callable[[list], dict]) -> int:
    rucksacks = splitting_function(file_directory)
    sum_priorities = 0

    for rucksack in rucksacks:
        common_items = common_matching_function(rucksack)
        sum_priorities += aggregation_function(common_items, priorities_dict)

    return sum_priorities


def display_results(file_directory: str) -> None:
    priorities_dict = generate_prio_dict()

    print(f"Part 1: Sum of priorities of common items per elf rucksack -> {priorities_aggregation(file_directory, priorities_dict, split_rucksacks_compartments, find_common_items_per_rucksack, assign_priorities)}")
    

display_results(FILE_DIR)