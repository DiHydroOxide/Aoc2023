import os
import sys


def create_folder_and_files(d):
    folder_name = "Day " + d

    # Create the folder
    os.makedirs(folder_name, exist_ok=True)

    # Define the content for the Python files
    python_file_content = ("file_name = 'puzzle-input.txt'\n"
                           "\n"
                           " = []\n"
                           " = {}\n"
                           " = 0\n"
                           "\n"
                           "with open(file_name, 'r') as f:\n")

    # Create part1.py
    with open(os.path.join(folder_name, 'part1.py'), 'w') as part1_file:
        part1_file.write(python_file_content)

    # Create part2.py
    with open(os.path.join(folder_name, 'part2.py'), 'w') as part2_file:
        part2_file.write(python_file_content)

    # Create puzzle-input.txt
    with open(os.path.join(folder_name, 'puzzle-input.txt'), 'w') as input_file:
        input_file.write("")


if __name__ == "__main__":
    # Check if the script is given exactly one argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py folder_name")
    else:
        day = sys.argv[1]
        create_folder_and_files(day)
        print(f"Folder '{day}' created with files part1.py, part2.py, and puzzle-input.txt.")
