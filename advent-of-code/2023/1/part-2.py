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
    end_index = 3
    stored_digits = []
    iteration = 0
    while True:
        if start_index >= len(text):
            break
        current_char = text[start_index]
        iteration += 1
        potential_digit = (file_input[start_index:end_index])

        # Adds digit to list if it is a number
        try:
            int_value = int(current_char)
            stored_digits.append(int_value)
            start_index += 1
            end_index = start_index + 3
        except ValueError:
            # If last three is'nt a digit break the loop
            # if (len(text) - start_index <= 3) and potential_digit not in valid_digits.keys():
            #     break
            if (end_index == len(text)):
                start_index += 1
            # If the five digits dont match any digits from valid_digits
            elif (len(potential_digit) > 5) and potential_digit not in valid_digits.keys():
                start_index += 1
                end_index = start_index + 3
            # If the potential_digit match a valid digit
            elif potential_digit in valid_digits.keys():
                stored_digits.append(valid_digits[potential_digit])
                start_index = end_index
                end_index = start_index + 3
            else:
                end_index += 1
    print(iteration)
    return stored_digits

# 1.    Kolla så det är minst tre tecken kvar mellan start index och totala stränglängden,
#       bara tre tecken kvar och ej en siffra, så får det vara slut
# 2.    Har potential index nått upp till 5 karaktärer utan att matcha en siffra, öka start index med +1 och fortsätt


file_input = "eightsixnine"
file_input = "7onevsffj78ninejcnnvgn65"
digits = convert_to_digits(file_input)
print(digits)
