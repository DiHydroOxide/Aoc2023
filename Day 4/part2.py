file_path = 'puzzle-input.txt'


def read_card(card):
    tmp = card.strip().split(':')[1].split("|")  # Get the numbers
    nums = {"winning": [int(e) for e in tmp[0].strip().split()], "have": [int(e) for e in tmp[1].strip().split()]}

    winning = 0
    for num in nums["have"]:
        if num in nums["winning"]:
            winning += 1

    return winning


cards = []

with open(file_path, 'r') as file:
    for line in file:
        cards.append({"have": 1, "won": read_card(line)})

total_cards = 0

for i in range(0, len(cards)):
    for k in range(0, cards[i]["have"]):
        for j in range(0, cards[i]["won"]):
            cards[i+j+1]["have"] += 1

    total_cards += cards[i]["have"]

print("Total amounts of cards is " + str(total_cards))
