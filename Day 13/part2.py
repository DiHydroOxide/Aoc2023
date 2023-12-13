file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'

patterns = []
ans = 0


def dump_pat():
	global patterns
	for p in patterns:
		for l in p:
			print(l)
		print()


def one_diff(str1, str2):
	return sum(c1 != c2 for c1, c2 in zip(str1, str2)) == 1


with open(file_name, 'r') as f:
	for pattern in f.read().split('\n\n'):
		patterns.append(pattern.split())

for p in patterns:

	# Check for horizontal reflection lines
	hor_refs = []
	for ref_idx in range(1, len(p)):  # For each reflection location
		ref = False
		diff = False
		# print(f"ref_idx = {ref_idx}")
		# print(f"Range = {[ref_idx, len(p) - ref_idx]}")
		for i in range(1, min([ref_idx, len(p) - ref_idx]) + 1):  # For each line to end of pattern
			# print(f"Checking if {p[ref_idx - i]} == {p[ref_idx + i - 1]}, i = {i}")
			line_one = p[ref_idx - i]
			line_two = p[ref_idx + i - 1]

			if one_diff(line_one, line_two) and not diff:  # One difference and we haven't used it
				diff = True
				ref = True
			elif line_one == line_two:  # Same line found
				ref = True
			else:
				ref = False
				break

		if ref and diff:  # Must have one difference
			hor_refs.append(ref_idx)  # Add num of rows above
			break  # Found the reflection line already

	ans += sum(100 * r for r in hor_refs)

	vert_refs = []
	for ref_idx in range(1, len(p[0])):
		ref = False
		diff = False
		# print(f"Ref idx = {ref_idx}")
		for i in range(1, min([ref_idx, len(p[0]) - ref_idx]) + 1):
			# print(f"Checking if {[c[ref_idx + i - 1] for c in p]} == {[c[ref_idx - i] for c in p]}, i = {i}")
			line_one = [c[ref_idx + i - 1] for c in p]
			line_two = [c[ref_idx - i] for c in p]

			if one_diff(''.join(line_one), ''.join(line_two)) and not diff:
				ref = True
				diff = True
			elif line_one == line_two:
				ref = True
			else:
				ref = False
				break
		# print(f"BREAK ref = {ref}")
		if ref and diff:
			vert_refs.append(ref_idx)
	# print(vert_refs)

	ans += sum(vert_refs)

print(f"Answer is {ans}")
