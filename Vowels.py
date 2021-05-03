def main():
	user_input = input()
	text = user_input.strip()
	vowel = 'a', 'e', 'i', 'o', 'u'
	
	print('\n' + 'These are vowel')
	for a in user_input:
		if a in  vowel:
			print(a)
	print('\n')
	print('These are consonant')
	for n in user_input:
		if n not in vowel:
			print(n)

if __name__ == "__main__":
	main()