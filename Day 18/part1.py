file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
ans = 0

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
trench = [(0, 0)]
boundary = 0

with open(file_name, 'r') as f:
    for line in f:
        d, n, _ = line.split()
        dr, dc = dirs[d]
        n = int(n)
        boundary += n
        row, col = trench[-1]
        trench.append((row + dr * n, col + dc * n))

A = abs(sum(trench[i][0] * (trench[i - 1][1] - trench[(i + 1) % len(trench)][1]) for i in range(len(trench)))) // 2
ans = (A - boundary // 2 + 1) + boundary

"""
https://en.wikipedia.org/wiki/Shoelace_formula
Gets area inside polygon using other Trapizoid formula

x = trench[i][0] 
y-1 - y+1 = trench[i - 1][1] - trench[(i + 1) % len(trench)][1]
Then / 2 (// to get int instead of float)

https://en.wikipedia.org/wiki/Pick%27s_theorem
We have the inside border values (Border point has area of 1m2 but int coords cut these in half)
So remove half the border 
A - boundary // 2 + 1 this gives strictly internal area

Then add the number of boundary points again since we counted them
"""

print(f"Answer is {ans}")
