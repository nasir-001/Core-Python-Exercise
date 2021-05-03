def main():

	user_input = input("Enter the first filename: ")
	user_input2 = input("Enter the second filename: ")

	fobj = open(user_input, 'r')
	allLines = fobj.readlines()
	fobj.close()

	fobj2 = open(user_input2, 'w')
	for eachline in allLines:
		fobj2.write(eachline)

if __name__ == "__main__":
	main()