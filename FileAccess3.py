def main():
	user_input = input("Enter the file name here: ")
	fobj = open(user_input, 'r')
	allLines = fobj.readlines()
	fobj.close()
	while True:
		for a in range(0, 26):
			print(allLines)
			nexts = input("Enter any key to continue: ")
			if nexts:
				continue
			else:
				break
		break

if __name__ == "__main__":
	main()