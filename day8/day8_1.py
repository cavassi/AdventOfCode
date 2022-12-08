with open("day8/test_data.txt", "r") as data:
    data = data.read()

data = data.split("\n")
trees = data[:]
sum = 0
num_of_trees = 0

for i in range(len(data)):
    data[i] = list(data[i])

for i in range(len(data)):
    for j in range(len(data[i])-1):
        if int(data[i][j]) < int(data[i][j+1]):
            continue
        else:
            print(trees[i][j:-1])