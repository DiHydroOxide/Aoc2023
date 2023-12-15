file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
ans = 0

with open(file_name, 'r') as f:
	hashes = f.read().split(',')

for h in hashes:
	tmp = 0
	for ch in h:
		tmp += ord(ch)
		tmp *= 17
		tmp = tmp % 256

	ans += tmp

print(f"Answer is {ans}")
