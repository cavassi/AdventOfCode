with open('day2/data.txt', 'r') as file:
    line = file.read()

line = line.rstrip().split("\n")

for round in range(len(line)):
    line[round] = line[round].split(" ")

def need_to_win(shape):
    if shape[0] == "A":
        shape[1] = "Y"
    elif shape[0] == "B":
        shape[1] = "Z"
    elif shape[0] == "C":
        shape[1] = "X"
    return shape

def need_to_draw(shape):
    if shape[0] == "A":
        shape[1] = "X"
    elif shape[0] == "B":
        shape[1] = "Y"
    elif shape[0] == "C":
        shape[1] = "Z"
    return shape

def need_to_lose(shape):
    if shape[0] == "A":
        shape[1] = "Z"
    elif shape[0] == "B":
        shape[1] = "X"
    elif shape[0] == "C":
        shape[1] = "Y"
    return shape

for round in range(len(line)):
    if line[round][1] == "X":
        line[round] = need_to_lose(line[round])
        continue
    if line[round][1] == "Y":
        line[round] = need_to_draw(line[round])
        continue
    if line[round][1] == "Z":
        line[round] = need_to_win(line[round])
        continue

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
        if shapes[1] == "X":
            total_score_from_round = 3
        elif shapes[1] == "Y":
            total_score_from_round = 6
        if shapes[1] == "Z":
            total_score_from_round = 0
    elif shapes[0] == "B":
        if shapes[1] == "X":
            total_score_from_round = 0
        elif shapes[1] == "Y":
            total_score_from_round = 3
        if shapes[1] == "Z":
            total_score_from_round = 6
    elif shapes[0] == "C":
        if shapes[1] == "X":
            total_score_from_round = 6
        elif shapes[1] == "Y":
            total_score_from_round = 0
        if shapes[1] == "Z":
            total_score_from_round = 3
    return total_score_from_round

for round in line:
    total_score_from_shapes += score_from_shape(round[1])
    total_score_from_round += check_round_winner(round)

print(total_score_from_round + total_score_from_shapes)