import os
'''
Grab first and last digits from "eightwothree" the result should be 83
                                "6eight7six" should be 66
'''


def file_lines_to_list(file):
    '''Return list which each index represent information from each row from a file'''
    outputList = []
    with open(file, "r") as file:
        for line in file:
            outputList.append(line.strip())
    return outputList


def convert_to_digits(text):
    '''Converts textformat "eightsixone" to [8, 6, 9]'''
    valid_digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    start_index = 0
    stored_digits = []
    for index, char in enumerate(file_input):
        potential_digit = (file_input[start_index:index] + char)

        if potential_digit in valid_digits.keys():
            stored_digits.append(valid_digits[potential_digit])
            start_index = index + 1

    return stored_digits

# 1.    Kolla så det är minst tre tecken kvar mellan start index och totala stränglängden,
#       bara tre tecken kvar och ej en siffra, så får det vara slut
# 2.    Har potential index nått upp till 5 karaktärer utan att matcha en siffra, öka start index med +1 och fortsätt


file_input = "eightsixnine"
digits = convert_to_digits(file_input)
print(digits)
