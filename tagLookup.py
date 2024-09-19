import os
import random

RDPS = []


def getProfilesTags(line):
	profiles = ""
	tags = ""
	for i in range(len(line)):
		if i % 2 == 1:
			tags += f"{splittedLine[i].strip()}\n"
		else:
			prof = "+OO+" if len(
			    splittedLine[i].strip()) == 0 else splittedLine[i].strip()
			profiles += f"{prof}\t"
	return [profiles, tags]


def checkTabExists(str):
	if str.count("\t") == 0:
		return False
	return True


def flatList(items: list):
	j = 0
	newList = []
	for i in range(len(items)):
		if isinstance(items[i], list):
			for k in range(len(items[i])):
				newList.append(items[i][k])
		else:
			newList.append(items[i])
	return newList


def getTabbedIndex(spl: list):
	for i in range(len(spl)):
		if checkTabExists(spl[i]):
			return i
	return -1


#file1 = open('seeds.txt', 'r')
#Lines = file1.readlines()

with open('seeds.txt', "r") as file:
	seeds = file.readlines()

for i in range(5):
	random.shuffle(seeds)

step = int(input("Your Step: "))


def create_profile(file_id, profiles, file_mode="w+"):
	file2 = open(f'output/profiles_{file_id}.txt', file_mode)
	file2.write(profiles)
	file2.close()


def create_file_tag(file_id, tags, file_mode="w+"):
	file3 = open(f'output/file_{file_id}.txt', file_mode)
	file3.write(tags)
	file3.close()


splittedLine = seeds[0].split("\t")

# print(splittedLine)

# getProfiles(splittedLine)
# exit(0)

st = 0

profiles = ""
tags = ""

drops = 1
while st < len(seeds):
	splitted = seeds[st].split('\t')

	exTab = getTabbedIndex(splitted)
	splitted[exTab] = splitted[exTab].split('\t')
	flattenRow = flatList(splitted)

	splittedLine = flattenRow
	[pro, tag] = getProfilesTags(splittedLine)

	profiles += f"{pro}\n"
	tags += tag
	if st == (step * drops) - 1 or st == len(seeds) - 1:
		tags = tags.replace("\n\n", "\n")
		create_profile(drops, profiles)
		create_file_tag(drops, tags)
		drops += 1
		profiles = ""
		tags = ""
	st += 1

print("Done Generating ✔")
