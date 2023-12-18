file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
ans = 0

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
trench = [(0, 0)]
boundary = 0

with open(file_name, 'r') as f:
    for line in f:
        _, _, x = line.split()
        x = x[2:-1]
        dr, dc = dirs["RDLU"[int(x[-1])]]
        n = int(x[:-1], 16)
        boundary += n
        row, col = trench[-1]
        trench.append((row + dr * n, col + dc * n))

A = abs(sum(trench[i][0] * (trench[i - 1][1] - trench[(i + 1) % len(trench)][1]) for i in range(len(trench)))) // 2
ans = (A - boundary // 2 + 1) + boundary

print(f"Answer is {ans}")
