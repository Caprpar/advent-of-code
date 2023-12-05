import os

def file_lines_to_list(file):
    '''Return list which each index represent information from each row from a file'''
    outputList = []
    with open(file,"r") as file:
        for line in file:
            outputList.append(line.strip())
    return outputList

def get_calibration_value_from_encryption(encryption):
    '''
    takes the first and the last digit from an encryption and returns the caluibrationvalue from it
    "bgxd2dvlnstwo3six1" becomes ==> (21) 
    "6fourfour" becomes ==> (66)
    '''
    # TODO Make function for below to avoid repetation
    # Adds first digit from the encryption

    def _get_digit(encryption, reversed = False):
        '''Gets either the first digit or last digit, if reveresed is set to True, it will get the last digit'''
        calibrationValue = ""
        encryption = encryption[::-1] if reversed else encryption

        for character in encryption:
            try:
                int_value = int(character)
                calibrationValue += character
                break
            except ValueError:
                pass
        return (calibrationValue)
    
    return int(_get_digit(encryption) + _get_digit(encryption, True))

# Getting the relative filepath
filename = "input.txt"
file = os.path.join(os.path.dirname(__file__), filename)

calibration_list = file_lines_to_list(file)
calibration_values = []

# Grabs calibrationvalue from encryption and adds value to calibration_values array
for calibration in calibration_list:
    calibration_values.append(get_calibration_value_from_encryption(calibration))

sum_of_calibration_values = sum(calibration_values)
input(sum_of_calibration_values)

