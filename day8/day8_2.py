with open("day8/data.txt", "r") as data:
    data = data.read()

view_range = 0
sum = 0
data = data.split("\n")
current_longest_viewrange = 0

for i in range(len(data)):
    data[i] = list(data[i])
    
for i in range(len(data)):
    for j in range(len(data)):
        data[i][j] = int(data[i][j])

def check_direction_right(i, j):
    view_range = 0
    for a in range(j, len(data)-1):
        if data[i][j] <= data[i][a+1]:
            view_range += 1
            return view_range
        view_range += 1
    return view_range


def check_direction_down(i, j):
    view_range = 0
    for a in range(i, len(data)-1):
        if data[i][j] <= data[a+1][j]:
            view_range += 1
            return view_range
        view_range += 1
    return view_range

def check_direction_left(i, j):
    view_range = 0
    for a in range(j, 0, -1):
        if data[i][j] <= data[i][a-1]:
            view_range += 1
            return view_range
        view_range += 1
    return view_range

def check_direction_up(i, j):
    view_range = 0
    for a in range(i, 0, -1):
        if data[i][j] <= data[a-1][j]:
            view_range += 1
            return view_range
        view_range += 1
    return view_range

# print(check_direction_right(1,1))
# print(check_direction_down(1,1))
# print(check_direction_left(1,1))
# print(check_direction_up(1,1))
# exit()
for i in range(1, len(data)-1):
    for j in range(1, len(data)-1):

        right = check_direction_right(i, j)

        down = check_direction_down(i, j)

        left = check_direction_left(i, j)

        up = check_direction_up(i, j)

        product = (right * left * down * up)
        # print(product)

        if product > current_longest_viewrange:

            current_longest_viewrange = product

print(current_longest_viewrange)
