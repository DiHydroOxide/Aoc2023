file_path = 'puzzle-input.txt'

seeds = []
seed_location = []
garden_map = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [],
              "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}

# destination source amount

with open(file_path, 'r') as f:
    key = None

    for i, line in enumerate(f):
        if i == 0:  # First line of seeds
            seeds = [int(e) for e in list((line.split(": ")[1]).split())]
        elif not line.strip():  # Empty Line
            key = None
        elif line.split()[0] in garden_map.keys():  # Start of new map part
            key = line.split()[0]
        elif key is not None:  # In a map so add values to map
            garden_map[key].append([int(e) for e in list(line.split())])

for seed in seeds:
    mapped_val = seed
    for k, g in garden_map.items():  # For each map
        for i, m in enumerate(g):  # For each list of values in the map
            if m[1] < mapped_val <= m[1] + m[2]:  # Between source start and source end
                mapped_val = m[0] + (mapped_val - m[1])  # Offset from source value
                break

    seed_location.append(mapped_val)

print(f"Closest location is {min(seed_location)}")
