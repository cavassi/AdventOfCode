with open("day7/test_data.txt", "r") as data:
    data = data.read()

data = data.split("\n")
tree = []
for i in range(1, len(data)):
    data[i] = data[i].split(" ")

def new_dict(i, data):
    created_list = []
    for j in range(i+1, len(data)):
        if data[j][0] != "$" and data[j][1] != "cd":
            created_list.append(data[j])
        else:
            return created_list

def change_dict(i, data):
    pass
for i in range(1, len(data)):
    if data[i][1] == "ls":
        tree.append(new_dict(i, data))
    

for i in range(1, len(tree)):
    print(tree[i])











# tree_list = []
# temp_list_name = ""
# current_directory = []

# def new_branch_tree():
#     pass

# def check_TODO(line):
#     if line[0] == "$":
#         pass

#     elif line[0] == "d":
#         pass

#     else:
#         line = line.split(" ")
#         line = line[0]

# for i in range(1, len(data)):
#     check_TODO(data[i])