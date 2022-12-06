with open("day6/data.txt", "r") as data:
    data = data.read()

def check_occurrences(list):
    for j in range(len(list)):
        if not list_to_check.__contains__(list[j]):
            list_to_check.append(list[j])
        if len(list_to_check) == 14:
            return True

for i in range(len(data)-1):
    list = data[i:i+14]
    list_to_check = []

    if check_occurrences(list):
        print(i+14)
        break