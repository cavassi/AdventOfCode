test = "2024/d04/test.txt"
input = "2024/d04/data.txt"

xmas_occurrences = 0

with open(input, 'r') as data:
    matrix = data.read().split("\n")

MATRIX_X = len(matrix[0])
MATRIX_Y = len(matrix)

# CHECKERS

def right_check(letter_index):
    return letter_index <= MATRIX_X - 4

def left_check(letter_index):
    return letter_index >= 3

def up_check(line_index):
    return line_index >= 3

def down_check(line_index):
    return line_index <= MATRIX_Y - 4

def up_right_check(line_index, letter_index):
    return line_index >= 3 and letter_index <= MATRIX_X - 4

def down_right_check(line_index, letter_index):
    return line_index <= MATRIX_Y - 4 and letter_index <= MATRIX_X - 4

def up_left_check(line_index, letter_index):
    return line_index >= 3 and letter_index >= 3

def down_left_check(line_index, letter_index):
    return line_index <= MATRIX_Y - 4 and letter_index >= 3

# HORIZONTAL/VERTICAL

def xmas_right(line_index, letter_index):
    if right_check(letter_index):
        string = ""
        for i in range(4):
            string += matrix[line_index][letter_index+i]
        return string == "XMAS"
    return False

def xmas_left(line_index, letter_index):
    if left_check(letter_index):
        string = ""
        for i in range(4):
            string += matrix[line_index][letter_index-i]
        return string == "XMAS"
    return False

def xmas_up(line_index, letter_index):
    if up_check(line_index):
        string = ""
        for i in range(4):
            string += matrix[line_index-i][letter_index]
        return string == "XMAS"
    return False

def xmas_down(line_index, letter_index):
    if down_check(line_index):
        string = ""
        for i in range(4):
            string += matrix[line_index+i][letter_index]
        return string == "XMAS"
    return False

# DIAGONAL

def xmas_up_right(line_index, letter_index):
    if up_right_check(line_index, letter_index):
        string = ""
        for i in range(4):
            string += matrix[line_index-i][letter_index+i]
        return string == "XMAS"
    return False

def xmas_up_left(line_index, letter_index):
    if up_left_check(line_index, letter_index):
        string = ""
        for i in range(4):
                string += matrix[line_index-i][letter_index-i]
        return string == "XMAS"
    return False

def xmas_down_right(line_index, letter_index):
    if down_right_check(line_index, letter_index):
        string = ""
        for i in range(4):
                string += matrix[line_index+i][letter_index+i]
        return string == "XMAS"
    return False


def xmas_down_left(line_index, letter_index):
    if down_left_check(line_index, letter_index):
        string = ""
        for i in range(4):
                string += matrix[line_index+i][letter_index-i]
        return string == "XMAS"
    return False

for line_index, line in enumerate(matrix):
    for letter_index, letter in enumerate(line):

        if xmas_right(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_left(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_up(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_down(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_up_right(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_down_right(line_index, letter_index):
            xmas_occurrences += 1
            
        if xmas_up_left(line_index, letter_index):
            xmas_occurrences += 1

        if xmas_down_left(line_index, letter_index):
            xmas_occurrences += 1

print(xmas_occurrences)