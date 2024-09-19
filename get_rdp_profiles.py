import os
import copy

list_profiles = []
RDPs = []


def sort_profiles(profile_list):
	# Sort the list using a custom key
	sorted_list = sorted(profile_list,
	                     key=lambda x: int(x.split('_')[1].split('.')[0]))
	return sorted_list


rdpCount = 0


drops = list(sort_profiles(list(filter(lambda x : "profile" in x, os.listdir("./output")))))


with open(f"./output/{drops[0]}",
          'r') as f:
	ln = f.readlines()
	rdpCount = len(ln[0].strip().split('\t'))

for i in range(rdpCount):
	RDPs.append([])


iter = 0
for filename in drops:
	rdp = list(map(lambda x: [], RDPs))
	with open(f"./output/{filename}", 'r') as f:
		lines = f.readlines()
		for ln in lines:
			for i in range(rdpCount):
				val = ln.split('\t')[i].strip()
				if val:
					rdp[i].append(val)
	for i in range(rdpCount):
		RDPs[i].append(rdp[i])
	iter += 1

for i in range(rdpCount):
	for pr in range(len(RDPs[i])):
		with open(f"./output/schedule/RDP{i+1}.txt", 'a+') as file:
			file.write("|".join(RDPs[i][pr]))
			file.write("\n")
