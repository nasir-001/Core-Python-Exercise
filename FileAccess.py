def main():
	user_input = (input("Enter Number and filename: ").split())
	lines = 0
	num_line = int(user_input[0])
	filename = str(user_input[1])
	fobj = open(filename, 'r')
	allLines = fobj.readlines()
	fobj.close()	

	for line in range(num_line):
		for eachline in allLines:
			pass
		lines += 1

	

if __name__ == "__main__":
	main()