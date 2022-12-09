with open("day8/data.txt", "r") as data:
    data = data.read()

data = data.split("\n")
sum = 0

for i in range(len(data)):
    data[i] = list(data[i])
    
for i in range(len(data)):
    for j in range(len(data)):
        data[i][j] = int(data[i][j])

def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def reverse_list(list):
    reversed = []
    for i in range(len(list)-1, -1 , -1):
        reversed.append(list[i])
    return reversed


def make_new_matrix(data):
    for i in range(len(data)):
        highest_value = -1
        for j in range(len(data)):
            if data[i][j] > highest_value:
                highest_value = data[i][j]
                continue
            else:
                data[i][j] = " "
    return data

left = data

up = rotate_matrix(left)

right = rotate_matrix(up)

down = rotate_matrix(right)


left = make_new_matrix(left)

down = make_new_matrix(down)

right = make_new_matrix(right)

up = make_new_matrix(up)

left = left

for i in range(1):
    down = rotate_matrix(down)

for i in range(2):
    right = rotate_matrix(right)

for i in range(3):
    up = rotate_matrix(up)

for i in range(len(data)):
    for j in range(len(data)):
        if left[i][j] == " " and down[i][j] == " " and right[i][j] == " " and up[i][j] == " ":
            sum += 1

print((len(data)*len(data))-sum)