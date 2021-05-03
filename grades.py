# Authur: Nasir Lawal
# Date: 21st-July-2019

# Description: Calculating grades from user input.

def main():

	# Collecting the score from user and compare 
	# the score using if elif and display the approprate result.
	num_list = []
	average = 0
	theStud = int(input("Please enter the number of the students here: "))
	for a in range(theStud):
		theScore = int(input("Please enter the score for each students: "))
		num_list.append(theScore)
		if theScore < 0:
			print("Score out of range")
		elif theScore < 60:
			print("Fail")
		elif theScore < 70:
				print("Grade D")
		elif theScore < 80:
			print("Grade C")
		elif theScore < 90:
			print("Grade B")
		elif theScore <= 100:
			print("Grade A")
		elif theScore > 100:
			print("Score out of range")
		if theScore:
			average += 1
		sum_list = sum(num_list)
		answer = sum_list / average
	
	print("The average is {:.2f}".format(answer))

if __name__ == "__main__":
	main()
