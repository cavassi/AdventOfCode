with open('Day 2/data.txt', 'r') as file:
    line = file.read()

line = line.rstrip().split("\n")

total_score_from_shapes = 0
total_score_from_round = 0

def score_from_shape(shape):
    if shape == "X":
        return 1 
    if shape == "Y":
        return 2 
    if shape == "Z":
        return 3

def check_round_winner(shapes):
    if shapes[0] == "A":
        if shapes[2] == "X":
            total_score_from_round = 3
        elif shapes[2] == "Y":
            total_score_from_round = 6
        if shapes[2] == "Z":
            total_score_from_round = 0
    elif shapes[0] == "B":
        if shapes[2] == "X":
            total_score_from_round = 0
        elif shapes[2] == "Y":
            total_score_from_round = 3
        if shapes[2] == "Z":
            total_score_from_round = 6
    elif shapes[0] == "C":
        if shapes[2] == "X":
            total_score_from_round = 6
        elif shapes[2] == "Y":
            total_score_from_round = 0
        if shapes[2] == "Z":
            total_score_from_round = 3
    return total_score_from_round

for round in line:
    total_score_from_shapes += score_from_shape(round[2])
    total_score_from_round += check_round_winner(round)

print(total_score_from_round + total_score_from_shapes)