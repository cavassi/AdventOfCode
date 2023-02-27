with open("day9/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split(" ")
    data[i][1] = int(data[i][1])

# for i in range(len(data)):
#     print(data[i])
################################

list_of_directions = []
s = set()

head = [0, 0]
tail = [0, 0]

for i in range(len(data)):
    for j in range(data[i][1]):
       if data[i][0] == "R":
            list_of_directions.append("R")
       if data[i][0] == "U":
            list_of_directions.append("U")
       if data[i][0] == "L":
            list_of_directions.append("L")
       if data[i][0] == "D":
            list_of_directions.append("D")

# for i in range(len(list_of_directions)):
#     print(list_of_directions[i])

for i in range(len(list_of_directions)):

    
    #HEAD MOVES
    if list_of_directions[i] == "R":
        head[0] += 1
    if list_of_directions[i] == "U":
        head[1] += 1
    if list_of_directions[i] == "L":
        head[0] -= 1
    if list_of_directions[i] == "D":
        head[1] -= 1
    # IN RANGE 1
    if head[0]-tail[0] in range(-1, 2) and head[1]-tail[1] in range(-1, 2):
        s.add((tail[0], tail[1]))
        continue

    #TAIL MOVES

    # 2 BLOCKS IN SAME DIRECTION
    if head[0]-tail[0] == 2 and head[1]-tail[1] == 0:
        tail[0] += 1
        s.add((tail[0], tail[1]))
        continue
    if head[1]-tail[1] == 2 and head[0]-tail[0] == 0:
        tail[1] += 1
        s.add((tail[0], tail[1]))
        continue
    if head[0]-tail[0] == -2 and head[1]-tail[1] == 0:
        tail[0] -= 1
        s.add((tail[0], tail[1]))
        continue
    if head[1]-tail[1] == -2 and head[1]-tail[1] == 0:
        tail[0] -= 1
        s.add((tail[0], tail[1]))
        continue
    
    #HORSE MOVE
    if head[0]-tail[0] >= 1 and head[1]-tail[1] >= 1:
        tail[0] += 1
        tail[1] += 1
        s.add((tail[0], tail[1]))
        continue
    if head[0]-tail[0] >= 0 and head[1]-tail[1] <= 0:
        tail[0] += 1
        tail[1] -= 1
        s.add((tail[0], tail[1]))
        continue
    if head[0]-tail[0] <= 0 and head[1]-tail[1] >= 0:
        tail[0] -= 1
        tail[1] += 1
        s.add((tail[0], tail[1]))
        continue
    if head[0]-tail[0] <= 0 and head[1]-tail[1] <= 0:
        tail[0] -= 1
        tail[1] -= 1
        s.add((tail[0], tail[1]))
        continue
# print(sorted(s))
print(len(s))