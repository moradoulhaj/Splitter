import os


def filter_single_profile(filepath):
  with open(filepath, 'r') as f:
    lines = f.readlines()

  maxLenLine = max(lines, key=len)
  totalLinesRec = maxLenLine.split("\t")

  processed_lines = list(map(lambda x: [], totalLinesRec))

  exp = '+OO+'
  for line in lines:
    processed_line = line.strip().split("\t")

    index = 0
    for col in processed_line:
      if col == exp:
        index += 1
        continue
      processed_lines[index].append(col)
      index += 1

  maxCol = 0
  minCol = 1000000
  for column in processed_lines:
    if len(column) > maxCol:
      maxCol = len(column)
    if len(column) < minCol:
      minCol = len(column)

  #exit(0)
  #"""

  newLines = []

  lenPr = len(processed_lines)
  for i in range(maxCol):
    arr = []
    for j in range(lenPr):
      if i < len(processed_lines[j]):
        arr.append(processed_lines[j][i])
      else:
        arr.append("")
    newLines.append(arr)

  lines = []

  def arrToStr(arr):
    t = ""
    for item in arr:
      t += f"{item}\t"
    return t

  nwStr = []
  for ln in newLines:
    nwStr.append(arrToStr(ln))
  with open(filepath, 'w') as file:
    file.write('\n'.join(nwStr))


def filter_profiles(directory):
  for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath) and "profile" in filepath:
      filter_single_profile(filepath)


directory_path = './output'
filter_profiles(directory_path)
