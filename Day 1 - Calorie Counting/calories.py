FILE_DIR = './calories.txt'

def read_list(file_directory):
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

def show_info(file_directory):
    elf_calories_list = format_calories_list(file_directory)
    
    total_elves = len(elf_calories_list)

    elf_with_max_calories = 0
    max_calories = 0
    for elf, calories in enumerate(elf_calories_list):
        calories_sum = sum(calories)

        if calories_sum > max_calories:
            max_calories = calories_sum
            elf_with_max_calories = elf

    return {
        'total_elves': total_elves,
        'elf_with_max_calories': elf_with_max_calories,
        'max_calories': max_calories
    }

print(show_info(FILE_DIR))