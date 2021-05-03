# Authur: Nasir Lawal
# Date: 28th-July-2019

# Description: Computing Quadratic Equation

import math
def main():
	Computing_Quadratic()
	

def Computing_Quadratic():
	user_input = input("Enter the values of a, b and c respectively: ")
	seprate = user_input.split(" ")

	a = int(seprate[0])
	b = int(seprate[1])
	c = int(seprate[2])

	if ((b ** 2) - (4 * a * c) / (2 * a > 0)) and ((b ** 2) - (4 * a * c) / (2 * a > a)):
		X1 = -b + math.sqrt( (b ** 2) - (4 * a * c) / 2 * a )
		X2 = -b - math.sqrt( (b ** 2) - (4 * a * c) / 2 * a )
		First = X1
		Second = X2

	else:
		print("Can't compute negative square root")

	def Print_Answer():
		print(First)
		print(Second)
	Print_Answer()

if __name__ == "__main__":
	main()