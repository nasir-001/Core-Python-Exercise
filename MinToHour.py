def main():

	def getMinute():
		user_input = int(input())
		if user_input < 60:
			print(str(user_input) + " " + "minute")
		elif user_input == 60:
			print("One Hour")
		elif user_input > 60 and user_input < 120:
			remainder = user_input - 60
			print("One Hour" + " " + str(remainder) + " minute")
	getMinute()

if __name__ == "__main__":
	main()
