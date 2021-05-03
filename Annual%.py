# Authur: Nasir Lawal
# Date: 25th-July-2019

# Description: Bank Account Interest Per per Year

def main():
	get_thePecentage()


# Function that accept a interest percentage rate and return the 
# total percentage per year, if the percentage is taken everyday.

def get_thePecentage(): # Function that collect the interest from user and perform the computation.
	percent = float(input("Enter the bank interest in percent: ")) # collecing and converting the integer to float
	Annual = 360 
	percentage = percent * Annual
	Answer = percentage

	def Display_Answer(): # Function that print only the string message and answer of our computation
		print("The total percent of the interest per year is " + str(Answer))
	Display_Answer()

if __name__ == "__main__":
	main()