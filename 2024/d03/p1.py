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


for part in parts:
    valid_part = extract_valid_part(part)
    if valid_part:
        product = calculate_product(valid_part)
        if product:
            total_sum += product

print(total_sum)
