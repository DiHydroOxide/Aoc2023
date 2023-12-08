from itertools import cycle
import math

file_name = 'puzzle-input.txt'

run_nodes = []
nodes = {}
ans = []

with open(file_name, 'r') as f:
    steps = f.readline().strip()
    f.readline()  # Blank Line

    for line in f.readlines():
        node = line.split(" = ")
        nodes[node[0]] = list(''.join(ch for ch in node[1].strip() if ch not in ['(', ')', ',']).split())
        if node[0][2] == 'A':
            run_nodes.append(node[0])

# Below here I cheated since I was at ~200 billion runs, ans was over 7.3 trillion
# We repeat through a cycle for some of the nodes until the number of steps to get there is a factor of every other path
# Find the length of all paths then find the lowest common multiple
# We can only find a node cycle if we have visited the node at the same point in the steps before

for node in run_nodes:  # FOr each node ending with 'A'
    visited = set()  # Set used to find a cycle

    # cnt = Number of times we have stepped, i = index of steps string we are at, d = direction of next step
    for cnt, (i, d) in enumerate(cycle(enumerate(steps)), start=1):
        prev, curr = node, nodes[node][d == "R"]  # Store the previous node and go to the new one
        visited.add((curr, i))  # Add the current new node and it's index in the steps to visited
        if prev.endswith('Z') and (curr, i) in visited:  # If we are at the end on a node cycle
            ans.append(cnt-1)  # Add the previous count to the ans since that is the length of this node cycle
            break  # Done 1 cycle of this node from '11A' -> '11Z' -> '11A'

print(f"Took {math.lcm(*ans)} steps")  # Get the lowest common multiple of each node cycle length
