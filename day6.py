f = open("input6")
data = f.readlines()
data.append("\n")

#1
forms = []
group = ""
for row in data:
	if row != "\n":
			group += row.strip("\n")
	else:
		forms.append(group)
		group = ""

answer = 0

for group in forms:
	yeses = set()
	for char in group:
		yeses.add(char)
	answer += len(yeses)

print(answer)

#2
groups = []
group = []
for row in data:
	if row != "\n":
		group.append(row.strip("\n"))
	else:
		groups.append(group)
		group = []

answer = 0

for group in groups:
	baseline = group[0]
	for char in baseline:
		everyone = True
		for individual in group:
			if not char in individual:
				everyone = False
		if everyone:
			answer += 1
print(answer)