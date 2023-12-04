file_path = 'puzzle-input.txt'

available = {"red": 12, "green": 13, "blue": 14}


def check_game(line):
    id_games = line.split(":")
    id = int(id_games[0].split()[1])
    game = id_games[1].strip().split(";")
    for g in game:
        cubes = g.split(',')
        for c in cubes:
            c = c.strip()
            num_col = c.split()
            print("Col = " + str(num_col[1]) + ", Cnt = " + str(num_col[0]))
            if int(num_col[0]) > available[num_col[1]]:
                return 0

    return id


total_games = 0

with open(file_path, 'r') as file:
    for line in file:
        total_games += check_game(line)

print("Total of game ID's is " + str(total_games))
