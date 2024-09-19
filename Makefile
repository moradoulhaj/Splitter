all:
	python set_entity.py
	python tagLookup.py
	python RemoveEmptyLines.py
	python listColumns.py
	python mergeFiles.py
	@read -p "Do you want to create Excel for Drops and Schedules? (Y/N): " yn; \
	if [ "$$yn" = "Y" ] || [ "$$yn" = "y" ]; then \
		python exceltest.py; \
		python get_rdp_profiles.py; \
		python createExcels.py; \
	fi
	#python exceltest.py 
	#python get_rdp_profiles.py
	#python createExcels.py
	python zipoutput.py


clear:
	rm seeds.txt
	touch seeds.txt
	rm -rf ./output/pro*
	rm -rf ./output/file*
	rm -rf ./output/schedule/*
	rm -f ./output/merged.txt
	rm -f ./output/sample.xlsx
	rm -f ./zippedOutput/*
	clear