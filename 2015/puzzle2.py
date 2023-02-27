with open("day2/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")
presents = []
total_ribbon = 0

smallest = 0
second_smallest = 0
biggest = 0

for i in range(len(data)):
    presents.append(data[i].split("x"))

for i in range(len(presents)):
    smallest = min(int(presents[i][0]),int(presents[i][1]),int(presents[i][2]))

    second_smallest = (int(presents[i][0]) + int(presents[i][1]) + int(presents[i][2])) -\
                        (smallest + max(int(presents[i][0]),int(presents[i][1]),int(presents[i][2])))

    biggest = max(int(presents[i][0]),int(presents[i][1]),int(presents[i][2]))

    total_ribbon += (2*(smallest + second_smallest) + (smallest*second_smallest*biggest))

print(total_ribbon)