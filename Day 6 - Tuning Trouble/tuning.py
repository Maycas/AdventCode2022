import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.utils import read_list

FILE_DIR = './data/datastream.txt'
DATASTREAM = read_list(FILE_DIR)[0]

def find_marker(datastream: str, buffer_length: int) -> int:
    for marker in range(buffer_length, len(datastream) + 1):
        to_check = datastream[marker - buffer_length: marker]
        if len(set(to_check)) == buffer_length:
            return marker  
    return -1

def display_results(datastream: str) -> None:
    print(f"Part 1 - Marker is in position {find_marker(datastream, 4)}")
    print(f"Part 2 - Marker is in position {find_marker(datastream, 14)}")


display_results(DATASTREAM)