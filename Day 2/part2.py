import math

file_path = 'puzzle-input.txt'


def check_game(line):
    id_games = line.split(":")
    id = int(id_games[0].split()[1])
    game = id_games[1].strip().split(";")
    available = {"red": 0, "green": 0, "blue": 0}

    for g in game:
        cubes = g.split(',')
        for c in cubes:
            c = c.strip()
            num_col = c.split()
            if int(num_col[0]) > available[num_col[1]]:
                available[num_col[1]] = int(num_col[0])

    return math.prod(available.values())


total_prod = 0

with open(file_path, 'r') as file:
    for line in file:
        total_prod += check_game(line)

print("The product of minimum cubes for all games is " + str(total_prod))
