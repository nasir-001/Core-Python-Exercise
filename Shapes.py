# Authur: Nasir Lawal
# Date: 28-July-2019

# Description: Function that calculate and returns the Area and the Volume of Shapes
def main():
	Circle()
	Spheres()
	Cubic()
	Square()

def Circle():
	User_input = float(input("Enter the radius of a circle: "))
	if User_input:
		Area = 2 * 3.141592653589793 * User_input ** 2
		radius = 3.141592653589793 * User_input ** 2

		print("The area of this circle is: " + str(Area))
		print("The radius of this circle is: " + str(radius) + "\n")

def Spheres():
	User_input = float(input("Enter the radius of the Sphere: "))
	if User_input:
		Area = 4 * 3.141592653589793 * User_input ** 2
		Volume = 4 / 3 * 3.141592653589793 * User_input ** 3

		print("The area of this sphere is: " + str(Area))
		print("The volume of the this sphere is: " + str(Volume) + "\n")


def Cubic():
	User_input = float(input("Enter the value of one side of the cube: "))
	if User_input:
		Area = 6 * User_input ** 2
		Volume = User_input ** 3

		print("The area of this cube is: " + str(Area))
		print("The volume od this cube is: " + str(Volume) + "\n")

def Square():
	User_input = float(input("Enter one side of the square: "))
	if User_input:
		Area = User_input ** 2
		Volume = User_input ** 3

		print("The area of this square is: " + str(Area))
		print("The volume of this square is: " + str(Volume))

if __name__ == "__main__":
	main()