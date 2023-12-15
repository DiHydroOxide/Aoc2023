file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
ans = 0

with open(file_name, 'r') as f:
	hashes = f.read().split(',')


def run_hash(h):
	tmp = 0
	for ch in h:
		tmp += ord(ch)
		tmp *= 17
		tmp = tmp % 256

	return tmp


def get_lens_command(h):
	lens = 0
	label = ''
	cmd = None

	for ch in h:
		if cmd is not None:
			lens = int(ch)
		elif ch in ['=', '-']:
			cmd = ch == '='
		else:
			label += ch

	return run_hash(label), (label, lens), cmd


boxes = {}

for h in hashes:
	box, lens, cmd = get_lens_command(h)

	# Add lens
	if cmd:
		if box not in boxes.keys():
			boxes[box] = [lens]
		else:
			for i, tup in enumerate(boxes[box]):
				if tup[0] == lens[0]:  # Update lens value
					boxes[box][i] = lens
					break
			else:
				boxes[box].append(lens)  # If no existing lens insert
	# Remove lens
	else:
		if box in boxes.keys():
			for tup in boxes[box]:
				if tup[0] == lens[0]:
					boxes[box].remove(tup)
					break

print(boxes)

for k, v in boxes.items():
	if v:  # If not empty box
		for i, lens in enumerate(v, start=1):
			ans += (k + 1) * i * lens[1]

print(f"Answer is {ans}")
