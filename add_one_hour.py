from datetime import datetime, timedelta


def add_one_hour(formatted_time):
	# Parse the datetime string back to a datetime object
	time_obj = datetime.strptime(formatted_time, "%d/%m/%Y %H:%M:%S %p")

	# Add one hour
	new_time_obj = time_obj + timedelta(hours=1)

	# Convert back to 24-hour format with AM/PM
	new_formatted_time = new_time_obj.strftime("%d/%m/%Y %H:%M:%S %p")

	return new_formatted_time
