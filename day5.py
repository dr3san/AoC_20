f = open("input5")
passes = [x.strip() for x in f.readlines()]

#1
seatIDmax = 0
for seat in passes:
	row = [0, 127]
	for i in range(7):
		if seat[i] == "B":
			row[0] += (2**6 / 2**i)
		elif seat[i] == "F":
			row[1] -= (2**6 / 2**i)
	
	column = [0, 7]
	for j in range(3):
		if seat[j+7] == "R":
			column[0] += 2**2 / 2**j
		elif seat[j+7] == "L":
			column[1] -= 2**2 / 2**j
	
	seatID = int(row[0] * 8 + column[0])
	seatIDmax = max(seatID, seatIDmax)

print(seatIDmax)

#2
plane = []
for i in range(127):
	row = ["o"] * 8
	plane.append(row)

for seat in passes:
	row = [0, 127]
	for i in range(7):
		if seat[i] == "B":
			row[0] += (2**6 / 2**i)
		elif seat[i] == "F":
			row[1] -= (2**6 / 2**i)
	
	column = [0, 7]
	for j in range(3):
		if seat[j+7] == "R":
			column[0] += 2**2 / 2**j
		elif seat[j+7] == "L":
			column[1] -= 2**2 / 2**j

	plane[int(row[0])][int(column[0])] = "x"

for row in plane:
	print(row)

for row in plane:
	for seat in row:
		if seat == "o":
			print(plane.index(row) * 8 + row.index(seat))