from collections import Counter
from copy import deepcopy

file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

with open(file_name, 'r') as f:
    grid = [line.strip() for line in f]


def swap(s, p1, p2):
    str_list = list(s)
    str_list[p1], str_list[p2] = s[p2], s[p1]
    return ''.join(str_list)


def roll_rocks(transposed_grid):
    for col_idx, col in enumerate(transposed_grid):
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

        transposed_grid[col_idx] = new_col

    return transposed_grid
    # return [''.join(chars) for chars in zip(*transposed_grid)]  # Return original grid


def get_weight(grid):
    a = 0
    for i, row in enumerate(grid):
        cntr = Counter(row)

        if 'O' in cntr.keys():
            a += cntr['O'] * (len(grid) - i)

    return a


def is_sublist(sublist, main_list):
    return any(sublist == main_list[i:i+len(sublist)] for i in range(len(main_list)-len(sublist)+1))


def find_repeating_sequence(numbers, min_sequence_length=4):
    list_length = len(numbers)

    for sequence_length in range(min_sequence_length, list_length):
        for i in range(list_length - sequence_length + 1):
            subsequence = numbers[i:i + sequence_length]

            # print(f"Check seq {subsequence} double is {subsequence * 2}")
            # Check if the subsequence repeats consecutively
            if is_sublist(subsequence * 2, numbers):
                return subsequence

    return None  # Return None if no repeating sequence is found


prev_grids = []
end_cycle = 0
seq = None

for cycle in range(1000000000):
    grid = roll_rocks([''.join(chars) for chars in zip(*grid)])  # North is Left of string
    grid = roll_rocks([''.join(chars) for chars in zip(*grid)])  # West is left side
    grid = roll_rocks([''.join(chars)[::-1] for chars in zip(*grid)])  # North is left then reverse so south is
    grid = roll_rocks([''.join(chars)[::-1] for chars in zip(*grid)][::-1])  # West is left then reverse so East is
    grid = [r[::-1] for r in grid]

    prev_grids.append(get_weight(grid))  # Add weight to list of weights

    seq = find_repeating_sequence(prev_grids)  # See if there is a repeating sequence of weights
    if seq:  # If we have a sequence
        end_cycle = cycle
        break

print(f"Weight after 1000000000 cycles is {seq[(1000000000 - end_cycle - 1) % len(seq) - 1]}")
