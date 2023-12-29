import re

file_name = 'puzzle-input.txt'
# file_name = 'sample.txt'
ans = 0

with open(file_name, 'r') as f:
	workflows, parts = f.read().split('\n\n')
	workflows = workflows.split()
	part_tmp = parts.split()

rules = {}
parts = []

for w in workflows:
	rule_str = re.search(r'{(.*?)}', w)
	rules[w.split('{', 1)[0]] = rule_str.group(1).split(',')

for p in part_tmp:
	parts.append(p.replace('{', '').replace('}', '').split(','))
	# parts.append({k: int(v) for k, v in (r.split('=') for r in tmp)})


def process(part, rule) -> int:
	global x, m, a, s

	for thing in part:  # Set variables
		exec(thing, globals())

	for r in rules[rule]:
		rule_pth = r.split(':')

		if len(rule_pth) == 2:
			exp, rs = rule_pth
		else:
			if rule_pth[0] == 'A':
				return sum([x, m, a, s])
			elif rule_pth[0] == 'R':
				return 0

			return process(part, rule_pth[0])

		if eval(exp):

			if rs == 'A':
				return sum([x, m, a, s])
			elif rs == 'R':
				return 0

			return process(part, rs)

	return 0


for p in parts:
	ans += process(p, 'in')

print(f"Ratings of accepted parts in {ans}")