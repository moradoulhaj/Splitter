import time
import os
import csv
from openpyxl import load_workbook
from datetime import datetime, timedelta

from add_one_hour import add_one_hour
from convert_time import convert_time
from zip_directory import zip_directory
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

RDPSINFO = []
entity = int(os.getenv('ENTITY'))

with open(f"./Sessions/CMH{entity}.csv", newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		RDPSINFO.append(row)

with open(f"./timedrops/CMH{entity}.txt") as file:
	timedrops = list(map(lambda x: x.strip(), file.readlines()))

rdpIndex = 1
for rdp in RDPSINFO:
	workbook = load_workbook('./template.xlsx')
	sheet = workbook.active
	ID = 1
	profiles = None
	with open(f"./output/schedule/RDP{rdpIndex}.txt") as file:
		profiles = list(map(lambda x: x.strip(), file.readlines()))
	for td in timedrops:
		ftime = convert_time(td)
		sheet[f"A{ID+1}"] = ID
		sheet[f"B{ID+1}"] = rdp['user']
		sheet[f"C{ID+1}"] = rdp['script']
		sheet[f"G{ID+1}"] = rdp['config']
		sheet[f"I{ID+1}"] = f"Drop {td}"
		sheet[f"H{ID+1}"] = 3
		sheet[f"E{ID+1}"] = ftime
		sheet[f"F{ID+1}"] = add_one_hour(ftime)
		sheet[f"D{ID+1}"] = profiles[ID - 1]
		ID += 1
	workbook.save(f"./output/schedule/RDP{rdpIndex}_{rdp['user']}.xlsx")
	rdpIndex += 1
