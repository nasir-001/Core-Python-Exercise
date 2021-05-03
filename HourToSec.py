# Authur: Nasir Lawal
# Date: 25th-July-2019

# Description: Conversion Of Hours To Seconds

def main():
	Get_Hours()

# Function for collecting the Hours and time from 
# user and then convert them into minutes.
def Get_Hours():
	hour = int(input("Enter the time in hours here: "))
	minutes = int(input("Enter the time in minutes here: "))
	MinToSec = minutes * 60
	HourToSec = hour * 60 * 60
	Answer = MinToSec + HourToSec
	print("The total time in second is " + str(Answer) + "secs")


if __name__ == "__main__":
	main()