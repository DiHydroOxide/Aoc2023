file_name = 'puzzle-input.txt'

ans = 0

with open(file_name) as f:
    oasis = [[int(v) for v in x.split()] for x in f.read().split("\n")]


def get_diff(oas):
    tmp = [sec - fir for fir, sec in zip(oas, oas[1:])]  # Get the differences of the list

    if all(e == tmp[0] for e in tmp):  # If all are the same value when we can return it, next will all be 0
        return oas[0] - tmp[0]
    else:
        return oas[0] - get_diff(tmp)  # Return first value - the difference of the next


for o in oasis:
    ans += get_diff(o)

print(f"Sum of Oasis extrapolation is {ans}")
