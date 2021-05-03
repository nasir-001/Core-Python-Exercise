def main():

	filename = input("Enter the name of the file here: ")
	fobj = open(filename, 'r')
	allLines = fobj.readlines()
	fobj.close()

	num = 0

	for eachline in allLines:
		pass
	for a in eachline:
		num += 1
		if num <= 80:
			print(a)

if __name__ == "__main__":
	main()
