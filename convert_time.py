from datetime import datetime, timedelta


def convert_time(input_time):
	# Get today's date
	today = datetime.today()  # e.g., 19/08/2024
	tomorrow = today + timedelta(days=1)  # e.g., 20/08/2024

	# Convert the input time string to a datetime object
	time_obj = datetime.strptime(input_time, "%H:%M")

	# Set the threshold time to 10:00 AM
	threshold_time = datetime.strptime("10:00", "%H:%M").time()

	# Determine the correct date based on the time provided
	if time_obj.time() >= threshold_time:  # For times from 10:00 AM onwards, use today's date
					date_with_time = datetime.combine(today, time_obj.time())
	else:  # For times before 10:00 AM, use tomorrow's date
					date_with_time = datetime.combine(tomorrow, time_obj.time())

	# Convert to 24-hour format with AM/PM
	formatted_date_time = date_with_time.strftime("%d/%m/%Y %H:%M:%S %p")

	return formatted_date_time
