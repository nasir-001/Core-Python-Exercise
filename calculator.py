# Authur: Nasir Lawal
# Date: 24th-July-2019

# Description: Computing two numbers from users input

def main():

	# Collecting operands and the operator from the user
	user_input = input("Enter numbers [Format==> N1 OP N2]\n")
	# Seperating the opernd for the operator using .split
	seperator = user_input.split(" ")
	# Assigning and converting the string to integer before operation
	a = int(seperator[0])
	b = int(seperator[2])
	operator = seperator[1]

	# Operands condition and operations to perform here.
	if operator == "+":
		print(a + b)
	elif operator == "-":
		print(a - b)
	elif operator == "/":
		print(a / b)
	elif operator == "*":
		print(a * b)
	elif operator == "**":
		print(a ** b)
	elif operator == "^":
		print(a ^ b)

if __name__ == "__main__":
	main()