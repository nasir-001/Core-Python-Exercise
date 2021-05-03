def main():
	
	num_list = []
	user_input = int(input())
	for a in range(user_input):
		num_list.append(int(input().strip()))
	first = num_list[0]
	second = num_list[1]
	third = num_list[2]

	for n in range(first, second+4, third):
		print(n)

if __name__ == "__main__":
	main()