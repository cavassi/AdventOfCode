with open("day2/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")

for i in range(len(data)):
    data[i] = data[i].split("x")

smallest = 0
middle = 0
biggest = 0

paper = 0

for i in range(len(data)):

    smallest = min(int(data[i][0]), int(data[i][1]), int(data[i][2]))
    biggest = max(int(data[i][0]), int(data[i][1]), int(data[i][2]))
    middle = (int(data[i][0]) + int(data[i][1]) + int(data[i][2])) - (smallest + biggest)

    paper += 2*(smallest*middle+middle*biggest+biggest*smallest) + (smallest*middle)


print(paper)