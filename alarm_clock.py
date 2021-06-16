import datetime

from playsound import playsound

alarmHour = int(input("What time do you want to wake up ?"))
alarmMinute = int(input("What minute do you want to wake up ?"))
amPM = str(input("am or pm ?"))

print("Waiting for alarm",alarmHour,alarmMinute,amPM)

if(amPM == "pm") :
	alarmHour = alarmHour + 12

while(True):
	if(alarmHour == datetime.datetime.now().hour and
		alarmMinute == datetime.datetime.now().minute):
		print("Wake up !!!")
		playsound("Ringtone.mp3")
		# nice bro
		#good bro
		break

print("exited")

