import sys, os, inspect
from typing import Callable
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

FILE_DIR = './data/warehouse.txt'


def create_stacks_from_input(file_dir):
    pass

def create_stack_moves_dict_from_input(file_dir):
    pass

def operate_crane(stacks, moves):
    pass

def unload_ships(file_dir):
    pass


print(unload_ships(FILE_DIR))