with open("day1/data.txt", "r") as data:
    floors = data.read()

left = 0
right = 0

for i in range(len(floors)):
    if floors[i] == "(":
        left += 1
    if floors[i] == ")":
        right += 1

print(abs(right-left))