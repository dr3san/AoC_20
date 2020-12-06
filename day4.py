f = open("input4")
data = f.readlines()#[line.strip("\n") for line in f.readlines()]
data.append("\n")

passports = []
passport = ""
for row in data:
	if row != "\n":
			passport += row.strip("\n") + " "
	else:
		passports.append(passport)
		passport = ""

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	
#1
validPassports = 0
for passport in passports:
	valid = True
	for field in fields:
		if not field in passport:
			valid = False
	if valid:
		validPassports += 1

print(validPassports)

#2
validEyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
import re
validPassports = 0
for passport in passports:
	validFields = True
	for field in fields:
		if not field in passport:
			validFields = False
	if validFields:
		prindi = False
		passportData = dict.fromkeys(fields)
		passport = passport.split()
		#could optimize if sort both fields and passport
		for field in passport:
			for label in fields:
				if label in field:
					passportData[label] = field[4:]
		validData = True
		if not int(passportData["byr"]) >= 1920 and int(passportData["byr"]) <= 2002 and len(passportData["byr"]) == 4:
			validData = Falseprint("viga1")
			#print("viga1")
		if not int(passportData["iyr"]) >= 2010 and int(passportData["iyr"]) <= 2020 and len(passportData["iyr"]) == 4:
			validData = False
			#print("viga2")
		if not int(passportData["eyr"]) >= 2020 and int(passportData["eyr"]) <= 2030 and len(passportData["eyr"]) == 4:
			validData = False
			#print("viga3")
		if passportData["hgt"][-2:] == "cm":
			if not int(passportData["hgt"][:-2]) >= 150 and int(passportData["hgt"][:-2]) <= 193:
				validData = False
				print("viga")
		elif passportData["hgt"][-2:] == "in":
			if int(passportData["hgt"][:-2]) >= 59 and int(passportData["hgt"][:-2]) <= 76 and len(passportData["hgt"]) == 4:
				validData = False
				print("viga")
		else:
			#print("Läks")
			validData = False
		if re.search("^#([0-9a-f]){6}$", passportData["hcl"]) == None:
			validData = False
			#print("viga4")
		if not passportData["ecl"] in validEyecolor:
			validData = False
			#print("viga5")
		if not passportData["pid"].isnumeric() and len(passportData["pid"]) == 9:
			validData = False
			#print("viga6")
		if validData:
			print(passportData)
			validPassports += 1
		
print(validPassports)