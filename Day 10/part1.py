file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

# | = Vert, - Hor, L NE, J NW, 7 SW, F SE, . Ground, S = Start
ans = 1
rows = []
start = [-1, -1]

pipe_transform = {'|': [0, 1], '-': [1, 0], 'L': [1, -1], 'J': [-1, -1], '7': [-1, 1], 'F': [1, 1]}

with open(file_name, 'r') as f:
    for line in f.readlines():
        rows.append(line.strip())


# Transverse to the next pipe
def move(pos, prev):
    pipe = rows[pos[0]][pos[1]]  # Get the pipe we are on
    print(f"Moving through a {pipe} at {pos} with previous as {prev}")

    new = None

    match pipe:
        case '|':
            new = [pos[0] + 1 if prev[0] < pos[0] else pos[0] - 1, pos[1]]  # If we moved up
        case '-':
            new = [pos[0], pos[1] + 1 if pos[1] > prev[1] else pos[1] - 1]  # If we moved in from left
        case 'L':
            if pos[0] != prev[0]:
                new = [pos[0], pos[1] + 1]  # +1 X
            else:
                new = [pos[0] - 1, pos[1]]  # -1 Y
        case 'J':
            if pos[0] != prev[0]:
                new = [pos[0], pos[1] - 1]  # -1 X
            else:
                new = [pos[0] - 1, pos[1]]  # -1 Y
        case '7':
            if pos[0] != prev[0]:
                new = [pos[0], pos[1] - 1]  # -1 X
            else:
                new = [pos[0] + 1, pos[1]]  # +1 Y
        case 'F':
            if pos[0] != prev[0]:
                new = [pos[0], pos[1] + 1]  # +1 X
            else:
                new = [pos[0] + 1, pos[1]]  # +1 Y
        case _:
            print(f"FUCK found a {pipe}")

    return new, pos


for x, row in enumerate(rows):
    try:
        y = row.index("S")
        start = [x, y]

        break
    except ValueError:
        continue

paths = []

if rows[start[0] + 1][start[1]] in ['|', 'L', 'J']:
    paths.append([start[0] + 1, start[1]])

if rows[start[0] - 1][start[1]] in ['|', '7', 'F']:
    paths.append([start[0] - 1, start[1]])

if rows[start[0]][start[1] + 1] in ['-', '7', 'J']:
    paths.append([start[0], start[1] + 1])

if rows[start[0]][start[1] - 1] in ['-', 'L', 'F']:
    paths.append([start[0], start[1] - 1])

prev = [start, start]

while True:
    # print(f"{paths[0]} is a {rows[paths[0][0]][paths[0][1]]}")
    paths[0], prev[0] = move(paths[0], prev[0])
    paths[1], prev[1] = move(paths[1], prev[1])
    ans += 1

    if paths[0] == paths[1]:
        break

    if ans % 10000 == 0:
        print(f"Been through {ans} pipes")

print(f"Furthest point is {ans} steps from start")
