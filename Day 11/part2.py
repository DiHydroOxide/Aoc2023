file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

universe = []
galaxy = []  # List of row, col of galaxies
empty = {"row": [], "col": []}  # Row/col values to check and add 1 mil to path

ans = 0

def pnd():
    print(galaxy)
    for g in universe:
        print(g)


with open(file_name, 'r') as f:
    for line in f.readlines():
        universe.append(line.strip())

        if set(line.strip()) == {'.'}:  # If only "." add another line
            empty['row'].append(len(universe) - 1)  # Index of empty row

empty_cols = []
for col in range(len(universe[0])):
    point = set()

    for row in universe:
        point.add(row[col])

    if point == {'.'}:
        empty["col"].append(col)  # Add empty cols to dict

# Find locations of galaxies
for i, row in enumerate(universe):
    for col in range(len(row)):
        if row[col] == '#':  # Add Galaxy to list
            galaxy.append([i, col])

print(empty)

for i, gal_one in enumerate(galaxy):
    for gal_two in galaxy[i+1:]:  # All Galaxies we haven't been to already
        # print(f"Gal_one = {gal_one}, Gal_two = {gal_two}")
        rows = list(range(gal_one[0]+1, gal_two[0]))

        if gal_one[1] > gal_two[1]:
            cols = list(range(gal_two[1] + 1, gal_one[1]))
        else:
            cols = list(range(gal_one[1] + 1, gal_two[1]))
        # print(f"Rows = {rows}, Cols = {cols}")
        ans += abs(gal_two[0] - gal_one[0]) + abs(gal_two[1] - gal_one[1])

        for r in rows:
            if r in empty['row']:
                ans += 999999  # Already adding the original star so we don't need to add it here

        for c in cols:
            if c in empty['col']:
                ans += 999999

print(f"Shortest distance between all pairs of galaxies is {ans}")
# pnd()
