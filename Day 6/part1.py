file_path = 'puzzle-input.txt'

races = []
beat = 1

with open(file_path, 'r') as f:
    key = None

    times = (f.readline().split(':')[1]).split()
    record = (f.readline().split(':')[1]).split()

for i in range(len(times)):
    races.append([int(times[i]), int(record[i])])

for race in races:
    time = race[0]
    distance = race[1]
    soonest = None
    latest = None

    for speed in range(1, time):
        # Soonest
        if soonest is None and speed * (time - speed) > distance:
            soonest = speed
        # Latest
        if latest is None and (time - speed) * (time - (time-speed)) > distance:
            latest = time - speed

        if soonest is not None and latest is not None:
            beat *= ((latest - soonest) + 1)
            break

print(f"Multiple of ways to beat races is {beat}")