import os
import random

file1 = open('seeds.txt', 'r')
Lines = file1.readlines()

with open(seeds_file, "r") as file:
  seeds = file.readlines()

order = 0

while order > 2 or order < 1:
  order = int(
      input(
          """Please enter folder Tag Order\n enter 1 for (folder,TAG) \n enter 2 for (TAG,folder)\n : """
      ))

seeds_nbr = int(input("Number of seeds: "))
file_id = int(input("File ID to start with: "))

if order == 1:
  for i in range(len(Lines)):
    Lines[i] = ','.join(Lines[i].split())

if order == 2:
  for i in range(len(Lines)):
    revOrder = Lines[i].split()[::-1]
    Lines[i] = ','.join(revOrder)

print("shuffling file...")
for i in range(10):
  random.shuffle(Lines)

seeds_splited = []
tags = []
folders = []


def remove_duplicates(l):
  return list(set(l))


def clear_files():
  for i in range(1, 22):
    if os.path.exists(f"file_{i}.txt"):
      os.remove(f"file_{i}.txt")
    if os.path.exists(f"folder_{i}.txt"):
      os.remove(f"folder_{i}.txt")


def create_file(file_id, seeds_splited, file_mode):
  file2 = open(f'file_{file_id}.txt', file_mode)
  for seed in seeds_splited:
    file2.write("".join(seed) + "\n")
  file2.close()


def create_folder_file(file_id, folders, file_mode):
  file3 = open(f'folder_{file_id}.txt', file_mode)
  folders_edit = list(set(folders))
  for folder in folders_edit:
    file3.write("".join(folder) + "\n")
  file3.close()


def get_lines_count():
  with open('seeds.txt') as f:
    line_count = 0
    for line in f:
      line_count += 1
  return line_count


count = 1
totalLines = len(Lines)

clear_files()
for line in Lines:
  exploder = line.split(",")
  tags.append(exploder[1])
  folders.append(exploder[0])
  seeds_splited.append(line.strip())
  if len(seeds_splited) == seeds_nbr or count == totalLines:
    create_file(file_id, tags, "a")
    create_folder_file(file_id, folders, "a")
    file_id += 1
    seeds_splited.clear()
    tags.clear()
    folders.clear()
  count += 1
#last_id = file_id
#create_file(last_id, seeds_splited, "a")
print("Done Generating ✔")
