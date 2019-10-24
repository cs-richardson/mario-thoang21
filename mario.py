"""
Tung Hoang - 10/04/19
This program print out a double half-pyramid of a specific height that you
would normally see in a Mario game
"""
# Asking for user input and checking if the input meet the requirements
height = input("Height: ")

while not(height.isdigit()) or int(height) < 0 or int(height) > 23:
    height = input("Height: ")

height = int(height)

# Printing the pyramid
for i in range(1,height + 1):
    whiteSpace = " " * (height - i)
    blocks = "#" * i
    print(whiteSpace + blocks + " " + blocks)
    
