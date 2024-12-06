file = "2024/d06/data.txt"
test = "2024/d06/test.txt"

map = []

with open(test, 'r') as data:
    for line in data:
        map.append(line.strip())

def find_guard(map):
    for line in map:
        guard = ["^", ">", "v", "<"]
        for char in guard:
            if char in line:
                return [map.index(line), line.index(char)]
            
    return False

def get_dir(map, pos):
    return map[pos[0]][pos[1]]

def replace_char(map, pos, new_char):
    string_list = list(map[pos[0]])
    string_list[pos[1]] = new_char
    map[pos[0]] = "".join(string_list)

def turn_right(pos):
    if map[pos[0]][pos[1]] == "^":
        replace_char(map, pos, ">")
        return

    if map[pos[0]][pos[1]] == ">":
        replace_char(map, pos, "v")
        return

    if map[pos[0]][pos[1]] == "v":
        replace_char(map, pos, "<")
        return

    if map[pos[0]][pos[1]] == "<":
        replace_char(map, pos, "^")
        return


def check_obstacle(map, pos, dir):
    if dir == "v":
        try:
            if map[pos[0]+1][pos[1]] == "#":
                turn_right(pos)
        except:
            return
    if dir == "^":
        try:
            if map[pos[0]-1][pos[1]] == "#":
                turn_right(pos)
        except:
            return
    if dir == ">":
        try:
            if map[pos[0]][pos[1]+1] == "#":
                turn_right(pos)
        except:
            return
    if dir == "<":
        try:
            if map[pos[0]][pos[1]-1] == "#":
                turn_right(pos)
        except:
            return

def in_map(pos):
    if pos[0] >= len(map) or pos[1] >= len(map[0]) or pos[0] < 0 or pos[1] < 0:
        return False
    return True
visited = set()

def walk(map):

    pos = find_guard(map)
    dir = map[pos[0]][pos[1]]

    i = 0

    while find_guard(map):

        if map[6][3] == "#":
            pass

        if i == (len(map) * len(map[0])):
            return True
        
        i +=1

        old_pos = pos.copy()

        check_obstacle(map, pos, get_dir(map, pos))

        if not in_map(pos):
            break
        if get_dir(map, pos) == "^":
            dir = "^"
            pos[0] -= 1
        if not in_map(pos):
            break
        if get_dir(map, pos) == ">":
            dir = ">"
            pos[1] += 1
        if not in_map(pos):
            break
        if get_dir(map, pos) == "v":
            dir = "v"
            pos[0] += 1
        if not in_map(pos):
            break
        if get_dir(map, pos) == "<":
            dir = "<"
            pos[1] -= 1

        replace_char(map, old_pos, ".")
        replace_char(map, pos, dir)

        if find_guard(map):
            visited.add(tuple(find_guard(map)))
        
    return False

map_x = len(map[0])
map_y = len(map)
loops = 0

for i in range(map_x):
    for j in range(map_y):
        if map[i][j] == "^" or map[i][j] == ">" or map[i][j] == "v" or map[i][j] == "<":
            continue
        pos = [i,j]
        if pos == [6,3]:
            pass
        temp_map = map.copy()
        
        replace_char(temp_map, pos, "#") 

        if walk(temp_map):
            loops += 1

print(loops)