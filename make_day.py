import os
import sys


def create_folder_and_files(d):
    folder_name = "Day " + d

    # Create the folder
    os.makedirs(folder_name, exist_ok=True)

    # Create part1.py
    with open(os.path.join(folder_name, 'part1.py'), 'w') as part1_file:
        part1_file.write("# file_name = 'puzzle-input.txt'\n"
                         "file_name = 'sample.txt'\n"
                         "ans = 0\n"
                         "\n"
                         "with open(file_name, 'r') as f:\n"
                         "\tgrid = [line.strip() for line in f]\n"
                         "\trow, grid = f.read().split('\\n\\n')\n"
                         "\n"
                         "print(f\"Answer is {ans}\")")

    for f in ['part2.py', 'puzzle-input.txt', 'sample.txt']:
        with open(os.path.join(folder_name, f), 'w') as input_file:
            input_file.write("")


if __name__ == "__main__":
    # Check if the script is given exactly one argument
    if len(sys.argv) != 2:
        print("Usage: python make_day.py <day>")
    else:
        day = sys.argv[1]
        create_folder_and_files(day)
        print(f"Folder '{day}' created")
