def main():
	user_input1 = int(input())
	name = []

	for a in range(user_input1):
		user_input2 = input("Enter name Format==> FN, LN ")
		for a in user_input2:
			if ',' not in user_input2:
				print("Wrong Format LastName, FirstName")
			break
		if ',' in user_input2:
			name.append(user_input2)
	print("The sorted list(by last name) is")
	sorted_name = sorted(name)
	for a in (sorted_name):
		print(a)
if __name__ == "__main__":
	main()