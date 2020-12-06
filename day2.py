f = open("input2")
content = f.readlines()#[int(line.strip()) for line in f.readlines()]

#1
correctPasswords = 0
for rule in content:
	amount = (int(rule.split()[0].split("-")[0]), int(rule.split()[0].split("-")[1]))
	counter = 0
	for char in rule.split()[2].strip():
		if char == rule.split()[1][0]:
			counter += 1
	if counter >= amount[0] and counter <= amount[1]:
		correctPasswords += 1
print(correctPasswords)

#2
import operator

correctPasswords = 0
for rule in content:
	positions = (int(rule.split()[0].split("-")[0])-1, int(rule.split()[0].split("-")[1])-1)
	if operator.xor(rule.split()[1][0] == rule.split()[2].strip()[positions[0]], rule.split()[1][0] == rule.split()[2].strip()[positions[1]]):
		correctPasswords += 1
print(correctPasswords)