import datetime
import time

while True:
	# Get the current time
	now = datetime.datetime.now()

	# Format the time as HH:MM:SS
	current_time = now.strftime("%H:%M:%S")

	# Clear the screen (for better display on the command line)
	print("\033c", end="")

	# Print the current time
	print("Digital Clock")
	print("=============")
	print(current_time)

	# Wait for one second
	time.sleep(1) 
