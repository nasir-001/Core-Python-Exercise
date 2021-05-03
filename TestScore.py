def main():

	user_input = input("Enter the file name here: ")
	fobj = open(user_input, 'r')
	allLines = fobj.readlines()
	fobj.close()

	for a in allLines:
		convert = int(a)
		print(convert)
		if convert < 0:
			print("Out of bound result " + a)
		if convert < 60:
			print("Fail")
		elif convert < 70:
			print("Grade D")
		elif convert < 80:
			print("Grade C")
		elif convert < 90:
			print("Grade B")
		elif convert <= 100:
			print("Grade A")
		else:
			print("Out of bound result " + a)

if __name__ == "__main__":
	main()