def main():

	user_input = input("Enter the type of transaction you want: ")
	Balance = 10000
	if user_input == "Widthrawal":
		Widthraw = int(input("How much will you like to Widthraw?: "))
		Balance -= Widthraw
		remain = balance - Widthraw
		print("\nYou have successifull Widthraw " + str(Widthraw) + " Naira")
		print("\nYour remaining balance is " + str(remain))
	elif user_input == "Inquiry":
		print(Balance)
	elif user_input == "Credit":
		Credit = int(input("How much will you like to Credit?: "))
		Balance += Credit
		add = Balance + Credit
		print("\nYou have successifull Credited " + str(Credit) + " Naira")
		print("\nYour remaining balance is " + str(add))


if __name__ == '__main__':
	main()