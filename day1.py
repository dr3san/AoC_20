f = open("input1")
content = [int(line.strip()) for line in f.readlines()]#[int(x) for f.readlines()]

#1
for count1, value1 in enumerate(content):
	for count2, value2 in enumerate(content):
		if count1 != count2 and value1 + value2 == 2020:
			print(value1)
			print(value2)
			print(value1*value2)
			break

#2
for count1, value1 in enumerate(content):
	for count2, value2 in enumerate(content):
		for count3, value3 in enumerate(content):
			if count1 != count2 and count2 != count3 and value1 + value2 + value3 == 2020:
				print(value1)
				print(value2)
				print(value3)
				print(value1*value2*value3)