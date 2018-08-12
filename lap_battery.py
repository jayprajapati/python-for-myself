#!/usr/bin/python
import time,subprocess
def calculate(power_full):
	power_now = open("/sys/class/power_supply/BAT0/energy_now", "r").readline()
	now= float(power_now)/float(power_full) * 100 
	return int(now)
def notify(message):
	subprocess.Popen(['notify-send',message])
	return
def main():

	power_full = open("/sys/class/power_supply/BAT0/energy_full", "r").readline()	

	m=1
	while 1:
		current=int(calculate(power_full))
		print "Charging : " + str(current) + "%"
		if m==2 or m==3 or m==4:

			status=open("/sys/class/power_supply/BAT0/status", "r").readline()	
			print status			
			if(status=='Charging\n'):			
				notify("100%!!!! Please Remove Charger!!")
				time.sleep(5)
				m=m+1	

		if current==100 and m==1:
			notify("Charging Completed!, Please Remove Charger")
			m=m+1
			time.sleep(10)
		print "sleep for 1 second.."
		time.sleep(1)
if __name__ == "__main__":
	main()
