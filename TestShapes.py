from Shapes import *

def get_Shapes():
	User_input = input("What did you want to compute? [Shapes == Circle, Square, Spheres and Cubes]: " + "\n")
	if User_input == "Circle":
		Circle()
	elif User_input == "Square":
		Square()
	elif User_input == "Spheres":
		Spheres()
	elif User_input == "Cubes":
		Cubic()
	else:
		print("Out of the list")
get_Shapes()