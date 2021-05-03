class Dollar:

	def getDollar():
		import math
		user_input = float(input())
		if user_input:
			num = math.ceil(user_input)
			str_num = str(num)
		print(str_num)


	getDollar()