from datetime import datetime
import time
from playsound import playsound

choice = int(input("Set an alarm?\n[1] Yes\n[2] No\n"))
print()

if choice == 1:
	hours = str(input("__:__\nEnter hours (0-23): "))
	minutes = str(input(f"{hours}:__\nEnter minutes (0-59): "))

	alarmTime = hours+":"+minutes

	print(alarmTime)

	while True:
		currentTime = datetime.now()
		if f"{currentTime.hour}:{currentTime.minute}" == alarmTime:
			break
		time.sleep(1)

	playsound("alarm.mp3")
	input()
	
else:
	quit()

# @XxGoOnViRxX#8734 and Etzeitet#4874
