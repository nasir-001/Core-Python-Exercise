# Authur: Nasir Lawal
# Date: 23rd-July-2019

# Description: Determine whether a year is a leap year or not a leap year

def main():

	# Collecting the year from the user
	Year = int(input("Enter any year: "))

	# Checking for all the conditions for the year to be Leap year.
	if (Year % 4 == 0 and Year % 100 != 0) or (Year % 4 == 0 and Year % 400 == 0):
		print("Leap year")

	# If the all the condition are evaluated to false then 
	# the given year from user is not a Leap year.
	else:
		print("Not a Leap year")

if __name__ == "__main__":
	main()