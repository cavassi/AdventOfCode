with open('day5/data.txt', 'r') as file:
    line = file.read()

line = line.split("\n\n")
line = line[1]
line = line.split("\n")
for i in range(len(line)):
    line[i] = line[i].strip('move ')
    line[i] = line[i].replace(' from ', " ")
    line[i] = line[i].replace(' to ', " ")
    line[i] = line[i].split(" ")

stack = [[],
        ["H", "C", "R"], 
        ["B", "J", "H", "L", "S", "F"], 
        ["R", "M", "D", "H", "J", "T", "Q"],
        ["S", "G", "R", "H", "Z", "B", "J"],
        ["R", "P", "F", "Z", "T", "D", "C", "B"],
        ["T", "H", "C", "G"],
        ["S", "N", "V", "Z", "B", "P", "W", "L"],
        ["R", "J", "Q", "G", "C"],
        ["L", "D", "T", "R", "H", "P", "F", "S"]]

# stack = [["A"],
#         ["Z", "N"],
#         ["M", "C", "D"],
#         ["P"]]

for i in range(len(line)):
    amount_to_move = int(line[i][0])
    move_from_stack = int(line[i][1])
    move_to_stack = int(line[i][2])
    line_i_length = len(stack[move_from_stack])

    for j in range((line_i_length - amount_to_move), line_i_length):
        stack[move_to_stack].append(stack[move_from_stack][j]) 

    for j in range((line_i_length - amount_to_move), line_i_length):
        stack[move_from_stack].pop()

str = ""
for i in range(1, len(stack)):
    str += stack[i][-1]
print(str)

