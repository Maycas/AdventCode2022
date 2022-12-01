FILE_DIR = './calories.txt'
TOP = 3

def read_list(file_directory: str) -> list:
    '''
    Reads a file inside a directory and returns a list 
    containing an item per line that has been read.

    Parameters
    ----------
    file_directory: str, mandatory
        The directory where the file to read the lines is 
        stored

    Returns
    ----------
    lines: list
        List containing a line per index

    Raises
    ----------
    FileNotFoundError
        If the file doesn't exist in the given directory
    '''
    with open(file_directory, 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]
    return lines

def format_calories_list(file_directory: str) -> list:
    '''
    Reads a file inside a directory and returns a 
    formatted list where each position contains a list
    of the item calories items carried by each elf.

    Parameters
    ----------
    file_directory: str, mandatory
        The directory where the file to read the lines is 
        stored.

    Returns
    ----------
    result: list
        Item calories items carried by each elf.
            E.g. [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    '''
    lines = read_list(file_directory)
    
    result = []
    elf_calories = []
    for line in lines:  
        if line != '':
            elf_calories.append(int(line))
        elif line == '':
            result.append(elf_calories)
            elf_calories = []
        else:
            print("Incorrect Value for 'calories.txt'")

    return result    

def maximum_calories_carrying_elf(elf_calories_list: list) -> tuple:
    '''
    Given a list of item calories per each elf, returns a
    tuple with the elf carrying the maximum number of calories
    and the sum of calories for all the items

    Parameters
    ----------
    elf_calories_list: list, mandatory
        A nested list where in each position there's a list
        containing the calories for each item in the list

    Returns
    ----------
    tuple
        Contains the elf carrying the highest amount of item
        calories and the calories sum
    '''
    elf_with_max_calories = 0
    max_calories = 0
    for elf, calories in enumerate(elf_calories_list):
        calories_sum = sum(calories)

        if calories_sum > max_calories:
            max_calories = calories_sum
            elf_with_max_calories = elf
    
    return elf_with_max_calories, max_calories

def maximum_calories_carrying_top_X_elves(elf_calories_list: list, X: int = 1) -> tuple[list]:
    '''
    Returns a tuple containing 2 lists:
        1 - The list of the top X elves carrying the items with the highest
        amount of calories
        
        2 - The sum of calories per each elf

    Each index in the lists corresponds to the same elf.

    Parameters
    ----------
    elf_calories_list: list, mandatory
        A nested list where in each position there's a list
        containing the calories for each item in the list

    X: int, optional
        Number of top elves to return as result. When not 
        informed is equal to 1

     Returns
    ----------
    tuple[list]
        List of tuples with the top elves carrying the highest 
        amount of items and another one with the calories sum
        for each elf.
    '''
    elves = []
    total_calories_carried_by_top_elves = []
    for _ in range(X):
        elf, calories = maximum_calories_carrying_elf(elf_calories_list)
        elves.append(elf)
        total_calories_carried_by_top_elves.append(calories)       
        
        # remove the max calories carrying elf from the list in next iteration
        elf_calories_list.pop(elf)

    return elves, total_calories_carried_by_top_elves


def show_info(file_directory: str, top: int = 1) -> dict:
    '''
    Reads a file inside a directory and returns a dictionary
    with a summary on the top elves carrying the biggest sum of 
    item calories.

    Parameters
    ----------
    file_directory: str, mandatory
        The directory where the file to read the lines is 
        stored

    top: int, optional
        Number of top elves to return as result. When not 
        informed is equal to 1

    Returns
    ----------
    dict: With the following keys
        total_elves: Number of elves going into expedition
        top_elves_with_max_calories: List of top calory carrying elves
        total_calories_carried_by_top_elves: List of the sum of all calories carried by each elf
        sum_total_calories: Sum of all the calories carried by the top elves
    '''
    elf_calories_list = format_calories_list(file_directory)
    total_elves = len(elf_calories_list)

    elves, total_calories_carried_by_top_elves = maximum_calories_carrying_top_X_elves(elf_calories_list, top)

    return {
        'total_elves': total_elves,
        'top_elves_with_max_calories': elves,
        'total_calories_carried_by_top_elves': total_calories_carried_by_top_elves,
        'sum_total_calories': sum(total_calories_carried_by_top_elves)
    }

print(show_info(FILE_DIR, TOP))