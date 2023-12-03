file_path = 'Aoc-Day3.txt'  # Replace 'your_file.txt' with the actual path to your text file

engine_num = 0
lines = []
part_nums = []


# If we find a number pass the index of the number and check for symbols around it and return the number
def check_symbol(lines, line_index, char_index_start, num_str):
    found_symbol = False

    for i in range(-1, 2):  # Go through the lines before and after
        if found_symbol:
            break

        if 0 <= line_index + i < len(lines):
            for j in range(-1, len(num_str)+1):
                if line_index + i < len(lines) and is_symbol(lines[line_index + i][char_index_start + j]):
                    found_symbol = True
                    part_nums.append({"num": int(num_str), "line": line_index, "char_start": char_index_start, "char_stop": char_index_start+len(num_str)-1})
                    break

    if found_symbol:
        return int(num_str)
    else:
        return 0


def is_digit(character):
    return character.isdigit()


def is_symbol(char):
    return not (char.isspace() or char.isalpha() or char.isdigit() or char == '.')


with open(file_path, 'r') as file:
    lines.append(file.readlines())

lines = lines[0]
dig = False

for line_index in range(0, len(lines)):
    for char_index in range(0, len(lines[line_index])):
        ch = lines[line_index][char_index]

        if is_digit(ch):
            if dig is not True:
                dig = True
                num_str = ch
                j = 0

                for i in range(1, 99):
                    new_ch = lines[line_index][char_index + i]
                    if is_digit(new_ch):
                        num_str += new_ch
                    else:
                        break

                engine_num += check_symbol(lines, line_index, char_index, num_str)
        else:
            dig = False

gear_ratio = 0
gear_tmp = []

for line_index in range(0, len(lines)):
    for char_index in range(0, len(lines[line_index])):
        ch = lines[line_index][char_index]
        gear_tmp = []

        if ch == '*':
            gear_parts = []
            ch_range = [char_index-1, char_index, char_index+1]
            for part in part_nums:
                if part['line'] - 1 <= line_index <= part["line"] + 1:
                    if part["char_start"] in ch_range or part["char_stop"] in ch_range:
                        gear_parts.append(part["num"])
                        gear_tmp.append(part)

            if len(gear_parts) == 2:
                gear_ratio += (gear_parts[0] * gear_parts[1])

print("Engine Number = " + str(engine_num))
print("Gear Ratio = " + str(gear_ratio))
