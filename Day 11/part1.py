file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

universe = []
galaxy = []  # List of row, col of galaxies

ans = 0

with open(file_name, 'r') as f:
    for line in f.readlines():
        universe.append(line.strip())

        if set(line.strip()) == {'.'}:  # If only "." add another line
            universe.append(line.strip())

empty_cols = []
for col in range(len(universe[0])):
    point = set()

    for row in universe:
        point.add(row[col])

    if point == {'.'}:
        empty_cols.append(col)

# Add new data to universe
for p in empty_cols[::-1]:  # Reverse to avoid changing indexes we still need to go through
    for i, row in enumerate(universe):
        universe[i] = row[:p] + "." + row[p:]

# Find locations of galaxies
for i, row in enumerate(universe):
    for col in range(len(row)):
        if row[col] == '#':  # Add Galaxy to list
            galaxy.append([i, col])


for i, gal_one in enumerate(galaxy):
    for gal_two in galaxy[i:]:  # All Galaxies we haven't been to already
        ans += abs(gal_two[0] - gal_one[0]) + abs(gal_two[1] - gal_one[1])

print(f"Shortest distance between all pairs of galaxies is {ans}")
# pnd()
