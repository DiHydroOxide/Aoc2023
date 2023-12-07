file_path = 'puzzle-input.txt'
card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
hands = {x: [] for x in range(1, 8)}


def get_type(s):
    char_counts = {}
    for ch in s:
        if ch not in char_counts.keys():
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1

    # print(f"Hand is {s} char_counts is {char_counts}")
    if len(char_counts) == 5:  # High Card
        return 1
    elif len(char_counts) == 4:  # Pair
        return 2
    elif set(char_counts.values()) == {2, 2, 1}:  # Two Pair
        return 3
    elif set(char_counts.values()) == {2, 3}:  # Full House
        return 5
    elif max(char_counts.values()) == 3:  # Three of a kind (Not Full House)
        return 4
    elif max(char_counts.values()) in [4, 5]:
        return max(char_counts.values()) + 2


with open(file_path, 'r') as f:
    for hand in f.readlines():
        h = hand.split()
        hands[get_type(h[0])].append(h)


def card_sort(item):
    return tuple(int(ch) if ch.isdigit() else card_map[ch] for ch in item[0])


new_hands = []

for k, v in hands.items():
    new_hands += sorted(v, key=card_sort)

val = sum((i+1) * int(hand[1]) for i, hand in enumerate(new_hands))
print(f"Total Winnings is {val}")
