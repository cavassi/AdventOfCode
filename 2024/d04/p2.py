test = "2024/d04/test.txt"
input = "2024/d04/data.txt"

MAS_indexes = []

with open(input, 'r') as data:
    matrix = data.read().split("\n")

MATRIX_X = len(matrix[0])
MATRIX_Y = len(matrix)

# CHECKERS

def up_right_check(line_index, letter_index):
    return line_index >= 2 and letter_index <= MATRIX_X - 3

def down_right_check(line_index, letter_index):
    return line_index <= MATRIX_Y - 3 and letter_index <= MATRIX_X - 3

def up_left_check(line_index, letter_index):
    return line_index >= 2 and letter_index >= 2

def down_left_check(line_index, letter_index):
    return line_index <= MATRIX_Y - 3 and letter_index >= 2

# DIAGONAL

def MAS_up_right(line_index, letter_index):
    if up_right_check(line_index, letter_index):
        string = ""
        for i in range(3):
            string += matrix[line_index-i][letter_index+i]
        if string == "MAS":
             MAS_indexes.append((line_index-1,letter_index+1))

def MAS_up_left(line_index, letter_index):
    if up_left_check(line_index, letter_index):
        string = ""
        for i in range(3):
                string += matrix[line_index-i][letter_index-i]
        if string == "MAS":
             MAS_indexes.append((line_index-1,letter_index-1))

def MAS_down_right(line_index, letter_index):
    if down_right_check(line_index, letter_index):
        string = ""
        for i in range(3):
                string += matrix[line_index+i][letter_index+i]
        if string == "MAS":
             MAS_indexes.append((line_index+1,letter_index+1))


def MAS_down_left(line_index, letter_index):
    if down_left_check(line_index, letter_index):
        string = ""
        for i in range(3):
                string += matrix[line_index+i][letter_index-i]
        if string == "MAS":
             MAS_indexes.append((line_index+1,letter_index-1))

for line_index, line in enumerate(matrix):
    for letter_index, letter in enumerate(line):

        MAS_up_right(line_index, letter_index)
        
        MAS_down_right(line_index, letter_index)
            
        MAS_up_left(line_index, letter_index)

        MAS_down_left(line_index, letter_index)



set_of_mas = set(MAS_indexes)

occurences = [MAS_indexes.count(coord) for coord in set_of_mas]

print(occurences.count(2))