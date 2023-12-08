import ast
file_name = 'puzzle-input.txt'

nodes = {}
ans = 0

with open(file_name, 'r') as f:
    steps = f.readline()
    f.readline()  # Blank Line

    for line in f.readlines():
        node = line.split(" = ")
        nodes[node[0]] = list(''.join(ch for ch in node[1].strip() if ch not in ['(', ')', ',']).split())

current_node = 'AAA'

while current_node != 'ZZZ':
    for step in steps:
        if step == 'L':
            current_node = nodes[current_node][0]
        elif step == 'R':
            current_node = nodes[current_node][1]

        if step in ['L', 'R']:
            ans += 1

print(f"Took {ans} steps")
