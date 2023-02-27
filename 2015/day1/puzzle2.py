with open("day1/data.txt", "r") as data:
    floors = data.read()

level = 0    

for i in range(len(floors)):
    if floors[i] == "(":
        level += 1
    if floors[i] == ")":
        level += -1
    if level == -1:
        break

print(i+1)