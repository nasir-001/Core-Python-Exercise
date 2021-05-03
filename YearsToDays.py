def main():

	def userInput():
		day, month, year = 0, 0, 0
		current_year = [7, 10, 2019]
		DD = current_year[0]
		MM = current_year[1]
		YY = current_year[2]
		user_input = list(map(int, input().split()))
		first = user_input[0]
		second = user_input[1]
		third = user_input[2]
		while first < DD and second < MM and third < YY:
			
			while first < current_year[0]:
				while True:
					first += 1
					break

			while second < current_year[1]:
				while True:
					second += 1
					break

			while third < current_year[2]:
				while True:
					third += 1
					break
			
			break
		
	userInput()

if __name__ == "__main__":
	main()