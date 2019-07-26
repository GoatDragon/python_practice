from time import sleep
from datetime import datetime

#ask for start time
start_time = input("start time in minutes: ")

#define starting hours and minutes based on input, set to zero if left blank
seconds = 0
try:
	hours = int(int(start_time) / 60)
	minutes = int(start_time) % 60
	total_minutes = int(start_time)
except ValueError:
	hours = 0
	minutes = 0
	total_minutes = 0

#write current time and date with starting conditions to log file
log_entry = "stopwatch was last ran at {} with start time {}h {}m\n".format(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), hours, minutes)
with open("/home/sam/Python/log_stopwatch", "a") as log:
    log.write(log_entry)
    
#stopwatch loop
while True:
	print("{}:{}:{} ({})".format(hours, minutes, seconds, total_minutes))
	sleep(1)
	seconds += 1
	if seconds == 60:
		minutes += 1
		total_minutes += 1
		seconds = 0
	if minutes == 60:
		hours += 1
		minutes = 0
