from collections import Counter
from copy import deepcopy

# file_name = 'puzzle-input.txt'
file_name = 'sample.txt'
ans = 0

with open(file_name, 'r') as f:
    grid = [line.strip() for line in f]


def dump(g):
    for row in g:
        print(row)
    print()


def swap(s, p1, p2):
    str_list = list(s)
    str_list[p1], str_list[p2] = s[p2], s[p1]
    return ''.join(str_list)


# Rotate grid 90 Deg so north is the left side of each string is north
grid = [''.join(chars) for chars in zip(*grid)]

for col_idx, col in enumerate(grid):
    new_col = deepcopy(col)  # Store a copy to change at end of loop
    for i, ch in enumerate(new_col):
        if ch == 'O' and i != 0:  # First element is north side
            new_idx = i
            for j in range(1, i + 1):  # Go from current position to left most valid
                if new_col[i - j] != '.':
                    new_idx = i - j + 1  # Go back one since we are at the end of a stack or
                    break
                else:
                    new_idx = i - j

            if i != new_idx:
                new_col = swap(new_col, i, new_idx)  # Swap i and new_idx in transposed_grid

    grid[col_idx] = new_col

grid = [''.join(chars) for chars in zip(*grid)]

for i, row in enumerate(grid):
    cntr = Counter(row)

    if 'O' in cntr.keys():
        ans += cntr['O'] * (len(grid) - i)

dump(grid)
print(f"Answer is {ans}")
