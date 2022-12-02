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