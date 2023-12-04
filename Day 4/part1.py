file_path = 'puzzle-input.txt'


def read_card(card):
    tmp = card.strip().split(':')[1].split("|")  # Get the numbers
    nums = {"winning": [int(e) for e in tmp[0].strip().split()], "have": [int(e) for e in tmp[1].strip().split()]}

    winning = 0
    for num in nums["have"]:
        if num in nums["winning"]:
            if winning == 0:
                winning = 1
            else:
                winning *= 2

    return winning


cards = []

with open(file_path, 'r') as file:
    for line in file:
        cards.append(read_card(line))

print("Cards are worth " + str(sum(cards)))
