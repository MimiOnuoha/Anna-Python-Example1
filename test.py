import csv

#this is importing the datetime type/class
from datetime import datetime

#importing the datetime module and renaming it "dt" 
#so it doesn't get confused with the above type 
import datetime as dt

from datetime import timedelta



current_time = datetime.now().strftime('%H:%M:%S')
fifteen_minutes = dt.datetime.now() + dt.timedelta(minutes=15)
future_time = fifteen_minutes.strftime('%H:%M:%S')



times =  open("stop_times.txt", 'rb')
reader = csv.reader(times)

def uptown():
	rownum = 0
	print "Next uptown trains from Classon: "
	
	for row in reader:
		#for northbound route 	
		if "WKD" in row[0] and row[3] == "G34N":
			traintimes = row[1]
			
			if traintimes > current_time and traintimes < future_time: 
				# print "Upcoming uptown train times: %s" %(traintimes[:5])
				print traintimes[:5]

def downtown():
	rownum = 0
	print "Next downtown trains from Classon: "

	for row in reader:
		#for southbound route 	
		if "WKD" in row[0] and row[3] == "G34S":
			traintimes = row[1]
			
			if traintimes > current_time and traintimes < future_time: 
				print traintimes[:5]




direction = raw_input("Downtown or uptown? ")
direction = direction.lower()
if direction == "downtown":
	downtown();
elif direction == "uptown":
	uptown();
else:
	print "Sorry, not a direction."

