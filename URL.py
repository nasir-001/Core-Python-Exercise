def main():

		while True:
		
			user_input = input("Enter operation you want to perform: ")
			URL_List = []
			if user_input == "Add":
				URL_List.append(input("Enter what you want to append: "))
			elif user_input == "Update":
				print(URL_List)
				removed = URL_List.append(input("Enter what you want to be Updated: "))
				URL_List.remove(removed)

				

if __name__ == "__main__":
	main()