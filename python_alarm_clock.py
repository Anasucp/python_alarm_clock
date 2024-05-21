from datetime import datetime
from playsound import playsound




alarm_time = input("Enter Tmie to set alarm:|HH:MM:SS:AM/Pm|:")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("alarm time is set:",alarm_time)




while True:
	now = datetime.now()
	current_hour = now.strftime("%I")
	current_minute = now.strftime("%M")
	current_second = now.strftime("%S")
	current_period = now.strftime("%P").upper()
	if (current_hour == alarm_hour and
		current_minute == alarm_min and
		current_second == alarm_sec and
		current_period == alarm_period):
		print("Wake up!")
		break
	
		
