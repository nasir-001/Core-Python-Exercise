def main():

	# collecting the user input in string form
	num_str = input("Enter a number: ")

	# converting the user input from string to integer
	num_num = int(num_str)

	# looping from 1 to the range of num_num + 1 and assign it to non_fact_list
	non_fact_list = range(1, num_num+1)
	num_list = list(non_fact_list)

	for a in num_list:
		print("Before:", repr(a))

	print("\n")

	# looping through num_list
	for n in num_list:
		# condition for n when divide by 2
		if n % 2 != 0:
			print("After:", repr(n))

if __name__ == "__main__":
	main()