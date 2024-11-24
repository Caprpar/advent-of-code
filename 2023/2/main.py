import os

def file_lines_to_list(file):
    '''Return list which each index represent information from each row from a file'''
    outputList = []
    with open(file,"r") as file:
        for line in file:
            outputList.append(line.strip())
    return outputList
