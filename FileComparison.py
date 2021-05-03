def main():

	filename1 = input("Enter the first file here: ")
	fobj1 = open(filename1, 'r')
	allLines = fobj1.readlines()
	fobj1.close()

	filename2 = input("Enter the second file here: ")
	fobj2 = open(filename2, 'r')
	allLines2 = fobj2.readlines()
	fobj2.close()

	lines = 0

	for a in filename1:
		for n in filename2:
			pass
		
		if a == n:
			lines += 1
		else:
			print(lines)
		

if __name__ == "__main__":
	main()