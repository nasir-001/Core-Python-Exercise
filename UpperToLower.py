def main():
	
	def getName():
		user_input = input()
		for a in user_input:
			lower = user_input.lower()
			if a == a.lower():
				print(a.upper())
			else:
				print(a.lower())
			

	getName()

if __name__ == "__main__":
	main()