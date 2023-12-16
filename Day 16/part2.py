file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

starting_lazer = []
ans = []


def dump(cont):
    for c in cont.values():
        print(c)


# Continue lazer on its path and return new (row, col)
def cont(diff, curr):
    return curr[0] + diff[0], curr[1] + diff[1]


with open(file_name, 'r') as f:
    contraption = {i: line.strip() for i, line in enumerate(f)}


for i in range(len(contraption)):
    starting_lazer.append([((i, -1), (i, 0))])
    starting_lazer.append([((i, len(contraption[0])), (i, len(contraption[0]) - 1))])

for i in range(len(contraption[0])):
    starting_lazer.append([((-1, i), (0, i))])
    starting_lazer.append([((len(contraption), i), (len(contraption) - 1, i))])

for lazer in starting_lazer:
    been = set()  # Energized tiles
    prev_lazer = set()
    while lazer:
        del_lazer = []
        add_lazer = []
        for i, (prev, current) in enumerate(lazer):  # For each lazer move forward
            if (prev, current) in prev_lazer or current[0] < 0 or current[0] >= len(contraption) or current[1] < 0 or \
                    current[1] >= len(contraption[0]):
                del_lazer.append(i)
                continue

            prev_lazer.add((prev, current))
            been.add(current)  # Add to tiles we have been
            tile = contraption[current[0]][current[1]]  # Current tile/mirror we are on
            diff = current[0] - prev[0], current[1] - prev[1]  # Change in the lazer path

            match tile:
                case '.':
                    new = cont(diff, current)
                case '-':
                    if diff[0] == 0:
                        new = cont(diff, current)
                    else:
                        new = current[0], current[1] + 1
                        add_lazer.append((current, (current[0], current[1] - 1)))
                case '|':
                    if diff[1] == 0:
                        new = cont(diff, current)
                    else:
                        new = current[0] + 1, current[1]
                        add_lazer.append((current, (current[0] - 1, current[1])))
                case '/':
                    new = current[0] - diff[1], current[1] - diff[0]
                case '\\':
                    new = current[0] + diff[1], current[1] + diff[0]
                case _:
                    print(f"FUCK {tile}")
                    exit()

            # print(f"Tile = {tile}, prev = {prev}, Current = {current}, NEW = {new}")

            lazer[i] = (current, new)
        else:
            for i in reversed(del_lazer):  # Delete largest index first
                del lazer[i]

            for t in add_lazer:
                lazer.append(t)

    ans.append(len(been))

print(f"Max energized {max(ans)} tiles")
