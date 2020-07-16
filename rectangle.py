# Ian Maze
# COP2002.0M1/0M2
# Feb, 9, 2020
# Area and Perimeter
# This program uses input from the user to calculate the area and perimeter
# of a rectangle




# Grabbing user's name -
print()
user_name = str(input("Please enter your name: "))




# Starting the program - Title
print()
print("Area/Perimeter of Rectangle Program!")
print("====================================")



#Grabbing data from user - Area/Perimeter
print()
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))




# Runing the calculations -
area = length * width
perimeter = length * 2 + width * 2




# Display calculated data -
print()
print("Area = " , area)
print("Perimeter = ", perimeter)




# Saying goodbye to user using collected user name -
print()
print(user_name + ", Thank you for using this program!")



