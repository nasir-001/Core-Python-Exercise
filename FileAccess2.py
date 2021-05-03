def main():
	filename = input("Enter Number and filename: ")
	lines = 0
	fobj = open(filename, 'r')
	allLines = fobj.readlines()
	fobj.close()	

	for eachline in allLines:
		lines += 1
	print(lines)

if __name__ == "__main__":
	main()