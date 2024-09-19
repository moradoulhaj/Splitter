st = "102	[A71922519DCFA6D1]			100	[DB2CBBCD544F0E8C]"


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


splitted = st.split("  ")

exTab = getTabbedIndex(splitted)
splitted[exTab] = splitted[exTab].split('\t')


flattenRow = flatList(splitted)

print(flattenRow)
