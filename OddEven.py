# Authur: Nasir Lawal
# Date: 26th-July-2019

# Description: Print all the Odd and Even numbers from 1 through 20.

def main():
	Even_Numbers()
	Odd_Numbers()
# Function that prints all the even numbers from 0 through 20 
# and 0 exclusive
def Even_Numbers():
	for a in range(0, 21, 2):
		if a == 0:
			pass
		else:
			print(a)
	print("\n")


# Function that prints all the odd number from 1 through 20.
def Odd_Numbers():
	for b in range(1, 20, 2):
		print(b)

if __name__ == "__main__":
	main()

