# This class manages the information for a linear mathematical
# function in the form:  y = mx + b

class LinearFunction:
    
    # Constructor - set attributes hours and payrate 
    def __init__(self, slope, y_int):
        self.slope = slope
        self.y_int = y_int

    def setSlope(self, x1, y1, x2, y2):
        self.slope = (y2 - y1) / (x2 - x1)

    def setSlope(self, newSlope):
        self.slope = newSlope
        
    def setYint(self, newInt):
        self.y_int = newInt
        
    def calcYfromX(self,x):
        return self.slope * x + self.y_int

    def getYintercept(self):
        return self.y_int

    def getXintercept(self):
        return -1 * self.y_int / self.slope
