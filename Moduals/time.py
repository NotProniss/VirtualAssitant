import datetime

def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like 
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	time = '''self,''' "The time is sir" + hour + "Hours and" + min + "Minutes"
	return time
 
def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number 
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		return("The day is " + day_of_the_week)