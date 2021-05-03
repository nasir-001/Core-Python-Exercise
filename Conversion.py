# Authur: Nasir Lawal
# Date: 25th-July-2019

# Description: Conversion of Fahrenheit to Celsius

def main():
	get_theTemperature()

# Function for collecting the temperature from user and 
# from Fahrenheit to Celcius 
def get_theTemperature(): 
	theTemperature = int(input("Enter the temperature in Fahrenheit: "))
	convertion = (theTemperature - 32) * (5 / 9)		
	Answer = convertion

	# Nested Function that inherits the convertion 
	# from the parent function and display the answer. 
	def Display_Answer():
		print(Answer)
	Display_Answer()

if __name__ == "__main__":
	main()