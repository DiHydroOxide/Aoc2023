file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

with open(file_name, 'r') as f:
    block1, _ = f.read().split('\n\n')

workflows = {}

for line in block1.splitlines():
    name, rule_str = line[:-1].split('{')  # Name of workflow and it's rules
    rules = rule_str.split(',')  # Each rule
    workflows[name] = ([], rules.pop())  # Add the last rule or fallback to end
    for rule in rules:
        comp, target = rule.split(':')  # Comparison string and target workflow
        key = comp[0]  # What val
        cmp = comp[1]  # < or >
        n = int(comp[2:])  # The rest is the number
        workflows[name][0].append((key, cmp, n, target))  # Add the comparison to the workflow rules


def process(ranges, name="in"):
    if name == 'R':  # If Rejected nothing to add
        return 0
    elif name == 'A':
        prod = 1
        for lo, hi in ranges.values():  # Multiply the ranges for the amount of combinations accepted
            prod *= hi - lo + 1
        return prod

    rules, fallback = workflows[name]  # Get current workflow
    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]  # lo, hi for the current range

        # Split the range into True and False parts with new ranges to check for

        if cmp == '<':  # If < then anything above will be False F
            T = (lo, min(n - 1, hi))  # Low to before target value
            F = (max(n, lo), hi)  # After target to high end of range
        else:
            T = (max(n + 1, lo), hi)  # After target to high end
            F = (lo, min(n, hi))  # Start to target

        if T[0] <= T[1]:  # If the range still contains something
            copy = dict(ranges)  # Copy for the next iteration to use
            copy[key] = T  # new True value for the range of the key
            total += process(copy, target)  # Call recursively

        if F[0] <= F[1]:
            ranges = dict(ranges)  # Copy ranges
            ranges[key] = F  # update the ranges in this iteration and move to next rule
        else:
            break
    else:
        total += process(ranges, fallback)  # If we didn't break move to default

    return total


print(f"Ratings of accepted parts in {process({key: (1, 4000) for key in "xmas"})}")
