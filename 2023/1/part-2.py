import os
import random


class Decoder:
    """The decoder to solve all elfs problem"""

    def __init__(self, filename="input.txt"):
        """Initialize data and decoded_lst"""
        self.filename = filename
        self.codes = self.get_data()
        self.decoded_lst = []
        self.random_code = self.get_random_code()
        self.valid_digits = {
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

    def get_data(self):
        """Return list of data from each row of the filename"""
        data = []
        file = os.path.join(os.path.dirname(__file__), self.filename)
        with open(file, "r") as file:
            for line in file:
                data.append(line.strip())
        return data

    def display_data(self):
        """Display the list of data"""
        print(self.data)

    def get_random_code(self):
        """Returns random code from the data list"""
        random_code = random.choice(self.codes)
        return random_code

    def get_allowed_chars(self, character_amount=3):
        '''gets the amount first chars from valid_digits to compare with the 
        code to encrypt'''
        char_list = []
        # character_amount -= 1
        for digit in self.valid_digits:
            char_list.append(digit[0:character_amount])
        return char_list

    def convert_code(self, code):
        """Returns digits from an encoded code like the example. 
        5zspmjkssghgtgpdpg3threeseven ==> [5, 3, 3, 7] """
        active = True
        decoded_list = []

        # Scan each char in sets of 3 then 4 then 5 to find out if the
        # characters is a valid digit.
        scan_len = 3
        index = 0
        while True:

            # Break the loop when scanned through every character from the code
            if index >= len(code):
                break

            current_char = code[index]

            try:
                int_input = int(current_char)
                decoded_list.append(int_input)

                index += 1  # Scan next char #TODO Can I convert this to a function?
                scan_len = 3

            except ValueError:
                current_scanned_char = code[index: scan_len + index]
                valid_scans = self.get_allowed_chars(scan_len)

                # save decoded digit if the scanned char is a valid digit
                if current_scanned_char in valid_scans and current_scanned_char in self.valid_digits:
                    decoded_list.append(
                        self.valid_digits[current_scanned_char])
                    index += 1  # Scan next char
                    scan_len = 3

                # increase scan_len if the chars has a potential digit
                elif current_scanned_char in valid_scans:
                    scan_len += 1  # ! Start here on new programming session

                # jump to next group of char to scan if current scan is invalid
                else:
                    index += 1

        return decoded_list

    def get_first_last_digit(self, decoded_list):
        '''Returns first and last indexes added to eachother as an int 
        [1,2,3] ==> 13 '''
        output = str(decoded_list[0]) + str(decoded_list[-1])
        return int(output)

    def decode_data(self):
        '''Decode data, as instructions from code of advent day 1 part 2'''
        for code in self.codes:
            decoded = self.convert_code(code)
            self.decoded_lst.append(self.get_first_last_digit(decoded))
        return sum(self.decoded_lst)


decoder = Decoder()
print(decoder.decode_data())
