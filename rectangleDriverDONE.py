# This program drives a Rectangle class by performing
# basic calculations.

from RectangleClassDONE import Rectangle

# Get user input
length = float(input("==> Enter rectangle length (meters): "))
width  = float(input("==> Enter retangle width (meters): "))

# Define and initialize object
myRectangle = Rectangle(length, width) 

# Perform calculations and capture results
area      = myRectangle.calcArea()
perimeter = myRectangle.calcPerimeter()
diagonal  = myRectangle.calcDiagonal()

# Build output message and display
outMessage = "\n"
outMessage += myRectangle.getDataAsString()    + "\n"
outMessage += "  Perimeter: " + str(perimeter) + " meters\n"
outMessage += "  Area:      " + str(area)      + " sq meters\n"
outMessage += "  Diagonal:  " + str(diagonal)  + " meters\n"

print(outMessage)
