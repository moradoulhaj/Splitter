import os


def fillNegatives(filelist, index):

  flNeg = []
  for file in filelist:
    with open(file, 'r') as file:
      lines = "".join(file.readlines())
      flNeg.append(lines)

  content = "\n__SEP__\n".join(flNeg)
  with open(f"./Negatives/output/1({index}).txt", 'w+') as file:
    file.write(content)


def remove_empty_lines_in_directory(directory):
  fileNames = os.listdir(directory)
  indx = 1
  mrgIndex = 1
  nglist = []
  for index in range(len(fileNames)):
    nglist.append(f"{directory}/{fileNames[index]}")
    if indx % 10 == 0 or index == len(fileNames) - 1:
      fillNegatives(nglist, mrgIndex)
      mrgIndex += 1
      nglist = []
    indx += 1


# Replace 'directory_path' with the path to your directory
directory_path = './Negatives'
maxFiles = 10
remove_empty_lines_in_directory(directory_path)
