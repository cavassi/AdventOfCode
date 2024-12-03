test = "2024/d03/test.txt"
input_file = "2024/d03/data.txt"

total_sum = 0

with open(input_file, 'r') as file:
    data = file.read()

parts = ["mul(" + part for part in data.split("mul(") if part]

def extract_valid_part(part):
    try:
        if ")" not in part:
            return None
        closing_index = part.index(")")
        return part[:closing_index + 1]
    except ValueError:
        return None

def calculate_product(part):
    part = part.replace("(", ",").replace(")", ",").split(",")
    if len(part) == 4 and part[1].isdigit() and part[2].isdigit():
        return int(part[1]) * int(part[2])
    return None

def chooser_check(part, chooser):
    chooser = chooser
    if "do()" in part:
        chooser = True
    if "don't()" in part:
        chooser = False
    if "do()" in part and "don't()" in part:
        if part.find("do()") < part.find("don't()"):
            chooser = False
        else:
            chooser = True
    return chooser

chooser = True

for part in parts:
    if chooser == True:
        valid_part = extract_valid_part(part)
        if valid_part:
            product = calculate_product(valid_part)
            if product:
                total_sum += product
    chooser = chooser_check(part, chooser)


print(total_sum)
