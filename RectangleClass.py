# This class manages the data and calculations of a rectangle.

class Rectangle:
    
    # Constructor - set attributes length and width 
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    # Method to return perimeter of this rectangle
    def calcPerimeter(self):
        return 2 * self.length + 2 * self.width
    
    # Method to return area of this rectangle
    def calcArea(self):
        return self.length * self.width  
    
    # Method to return diagonal of this rectangle
    def getDataAsString(self):
        outStr =  "Rectangle dimensions: " + str(self.length) + " meters X " 
        outStr +=  str(self.width) + " meters"
        return outStr
       
       
       
       
