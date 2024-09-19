import os

dirs = os.listdir("./output")

profiles = filter(lambda file: True if "pro" in file else False, dirs)
trimprofiles = lambda ln: ln.strip("\n")

drops = []
maxlength = 0


def sort_profiles(profiles):
	return profiles.sort()


sorted_profiles = list(profiles)


def read_lines(path):
	global maxlength
	global drops
	f = open(path, "r")
	lines = f.readlines()
	trimmed = list(map(trimprofiles, lines))
	maxlength = len(lines) if len(lines) > maxlength else maxlength
	drops.append(trimmed)


for fl in list(sorted_profiles):
	read_lines(f"./output/{fl}")

outputfile = open("./output/merged.txt", "a")
linesstr = ""

for i in range(maxlength):
	linesstr = ""
	for j in drops:
		if i in range(len(j)):
			linesstr += f"{j[i]}\t"
	outputfile.write(f"{linesstr}\n")

outputfile.close()
