file_path = 'puzzle-input.txt'

calibration_value = 0
num_map = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
key_list = list(num_map.keys())
value_list = list(map(str, list(num_map.values())))

# Read line and strip whitespace
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Go through each line
for line in lines:
    first = {"num": -1, "index": -1}
    last = {"num": -1, "index": -1}

    # Find the first and last occurrence of each possible number or string
    occurrences = {substring: [line.find(substring), line.rfind(substring)] for substring in key_list + value_list}

    # Find the lowest first value and highest last value in the occurrences
    for key, val in occurrences.items():

        # If the value is found and less than what we have
        if val[0] != -1 and (val[0] < first["index"] or first["index"] == -1):
            first["num"] = key
            first["index"] = val[0]

        if val[1] != -1 and val[1] > last["index"]:
            last["num"] = key
            last["index"] = val[1]

    # If we have a key in the list get the number as a string
    if first["num"] in key_list:
        first["num"] = str(num_map[first["num"]])

    if last["num"] in key_list:
        last["num"] = str(num_map[last["num"]])

    # If we have both then add to total
    if first["num"] != -1 and last["num"] != -1:
        calibration_value += int(first["num"] + last["num"])

print("Calibration value is " + str(calibration_value))