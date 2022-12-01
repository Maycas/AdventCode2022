FILE_DIR = './calories.txt'
TOP = 3

def read_list(file_directory):
    '''
    Reads a file inside a directory
    '''
    with open(file_directory, 'r') as file:
        lines = [line.strip('\n') for line in file.readlines()]
    return lines

def format_calories_list(file_directory):
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

def maximum_calories_carrying_elf(elf_calories_list):
    elf_with_max_calories = 0
    max_calories = 0
    for elf, calories in enumerate(elf_calories_list):
        calories_sum = sum(calories)

        if calories_sum > max_calories:
            max_calories = calories_sum
            elf_with_max_calories = elf
    
    return elf_with_max_calories, max_calories

def maximum_calories_carrying_top_X_elves(elf_calories_list, X):
    elves = []
    total_calories_carried_by_top_elves = []
    for _ in range(X):
        elf, calories = maximum_calories_carrying_elf(elf_calories_list)
        elves.append(elf)
        total_calories_carried_by_top_elves.append(calories)       
        
        # remove the max calories carrying elf from the list in next iteration
        elf_calories_list.pop(elf)

    return elves, total_calories_carried_by_top_elves


def show_info(file_directory, top = 1):
    elf_calories_list = format_calories_list(file_directory)
    total_elves = len(elf_calories_list)

    elves, total_calories_carried_by_top_elves = maximum_calories_carrying_top_X_elves(elf_calories_list, top)

    return {
        'total_elves': total_elves,
        'top_elves_with_max_calories': elves,
        'total_calories_carried_by_top_elves': total_calories_carried_by_top_elves,
        'sum_total_calories': sum(total_calories_carried_by_top_elves)
    }

print(show_info(FILE_DIR))