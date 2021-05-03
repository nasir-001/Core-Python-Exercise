def main():
	
	num_dict = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	}
	
	num_list = list(map(int, input().strip().split()))

	for a in num_dict.values():
		for b in num_list:
			if a == b:
				for n in num_dict.keys():
					dict_list = list(map(str, num_dict))
				print(dict_list[b-1] + "-" + dict_list[b-1])
				break

if __name__ == "__main__":
	main()