import sys, os, inspect
from typing import Callable
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

FILE_DIR = './data/assignments.txt'

def generate_zones(file_directory):
    lines = read_list(file_directory)
    
    # split elf zones
    sections = [line.split(',') for line in lines]
    # get beginning area and end area per zone
    sections = [[section[0].split('-'), section[1].split('-')] for section in sections]
    # cast strings to integers
    sections = [
        [
            [int(section[0][0]), int(section[0][1])],
            [int(section[1][0]), int(section[1][1])]
        ]
        for section in sections
    ]

    return sections

def count_subsets(file_directory):
    zones = generate_zones(file_directory)

    is_subset = 0
    for zone in zones:
        elf_1 = set(range(zone[0][0], zone[0][1] + 1))
        elf_2 = set(range(zone[1][0], zone[1][1] + 1))
        
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            is_subset += 1

    return is_subset

def count_overlaps(file_directory):
    zones = generate_zones(file_directory)

    is_overlap = 0
    for zone in zones:
        elf_1 = set(range(zone[0][0], zone[0][1] + 1))
        elf_2 = set(range(zone[1][0], zone[1][1] + 1))
        
        overlaps = elf_1.intersection(elf_2)
        if len(overlaps) > 0:
            is_overlap += 1

    return is_overlap


print(f"Part 1 - Number of subsets: {count_subsets(FILE_DIR)}")
print(f"Part 2 - Number of overlaps: {count_overlaps(FILE_DIR)}")