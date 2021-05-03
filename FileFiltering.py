def main():
	import os
	filename = input("Enter the filename here: ")
	if not os.path.exists(filename):
		with open(filename, 'w') as obj:
			obj.write("#This is comment in the file\n")
			obj.write("This is a text in the file\n")
			obj.write("This is another text in the file")
			allLines = obj.readlines()
		obj.close()
		print("The file does not exists")
		for a in allLines:
			if a == "#":
				pass
			else:
				print(a)

	else:
		print("\nThe file exists")
		obj = open(filename, 'r')
		allLines = obj.readlines()
		obj.close()
	for a in allLines:
		if a == "#":
			pass
		else:
			print(a)

if __name__ == "__main__":
	main()