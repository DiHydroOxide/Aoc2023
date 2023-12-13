file_name = 'puzzle-input.txt'
patterns = []
ans = 0

with open(file_name, 'r') as f:
	for pattern in f.read().split('\n\n'):
		patterns.append(pattern.split())

for p in patterns:

	# Check for horizontal reflection lines
	hor_refs = []
	for ref_idx in range(1, len(p)):  # For each reflection location
		ref = False
		for i in range(1, min([ref_idx, len(p) - ref_idx]) + 1):  # For each line to end of pattern
			if p[ref_idx - i] == p[ref_idx + i - 1]:  # If we have reflection
				ref = True
			else:
				ref = False
				break

		if ref:
			hor_refs.append(ref_idx)  # Add num of rows above

	ans += sum(100 * r for r in hor_refs)

	vert_refs = []
	for ref_idx in range(1, len(p[0])):
		ref = False
		for i in range(1, min([ref_idx, len(p[0]) - ref_idx]) + 1):
			if [c[ref_idx + i - 1] for c in p] == [c[ref_idx - i] for c in p]:
				ref = True
			else:
				ref = False
				break
		if ref:
			vert_refs.append(ref_idx)

	ans += sum(vert_refs)

print(f"Answer is {ans}")
