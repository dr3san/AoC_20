f = open("input3")
forest = [line.strip("\n") for line in f.readlines()]
width = len(forest[0])-1

#1,  2

treeses = []
movements = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for movement in movements:
	location = 0
	trees = 0
	for count, row in enumerate(forest):
		if count % movement[1] == 0:
			if location > width:
				location -= width + 1
			if row[location] == "#":
				trees += 1
			location += movement[0]

	treeses.append(trees)

for trees in treeses:
	print(trees)

product = 1
for trees in treeses:
	product *= trees

print(product)