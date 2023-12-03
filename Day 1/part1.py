file_path = 'puzzle-input.txt'

calibration_value = 0

# Read line and strip whitespace
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Go through each line
for line in lines:
    first = None
    last = None

    # Go through each char of the line until we find 2 digits
    for i in range(0, len(line)):
        # If we are looking for the first
        if line[i].isdigit() and first is None:
            first = line[i]

        # If we are looking for the last digit
        if line[-i-1].isdigit() and last is None:
            last = line[-i-1]

        # If we have both values add to the calibration and move on
        if first is not None and last is not None:
            calibration_value += int(first + last)
            break

print("Calibration value is " + str(calibration_value))