#Authur: Nasir Lawal
#Date: 21st-10-2019
#DEC BIN OCT HEX operators

def main():

	user_input1 = int(input("Enter the starting value: "))
	user_input2 = int(input("Enter the ending value: "))

	print("DEC		BIN		OCT		HEX")
	for a in range(user_input1, user_input2+1, 1):
		print(str(a) + "\t  " + str(bin(a)) + "\t\t" + str(oct(a)) + "\t\t" + str(hex(a)))

if __name__ == "__main__":
	main()