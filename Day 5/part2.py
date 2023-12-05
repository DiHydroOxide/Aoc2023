file_path = 'puzzle-input.txt'

seeds = []
garden_map = []

# destination source amount

with open(file_path, 'r') as f:
    key = -1

    for i, line in enumerate(f):
        if i == 0:  # First line of seeds
            tmp = list((line.split(": ")[1]).split())
            for index, val, in enumerate(tmp):
                if index % 2 == 0:
                    seeds.append([int(tmp[index]), int(tmp[index]) + int(tmp[index+1])])
        elif not line.strip():  # Empty Line
            pass
        elif line.split()[1] == "map:":  # Start of new map part
            key += 1
            garden_map.append([])
        else:
            garden_map[key].append([int(e) for e in list(line.split())])

garden_map.reverse()  # Reverse so location is first
garden_map[0].sort()

# Starting at smallest location check if we can map back to a seed

for location in garden_map[0]:  # For each location map
    # print(f"Checking location map {location}")
    for loc in range(location[0], location[0] + location[2] + 1):  # For the range of the map
        mapped_val = location[1] + loc
        for g in garden_map[1:]:  # For each map apart from the first (location)
            for i, m in enumerate(g):  # For each list of values in the map
                if m[0] < mapped_val <= m[0] + m[2]:  # Between source start and source end
                    mapped_val = m[1] + (mapped_val - m[0])  # Offset from source value
                    break

        for seed_pair in seeds:
            if seed_pair[0] <= mapped_val <= seed_pair[1]:
                print(f"Closest location is {loc}")
                exit()
