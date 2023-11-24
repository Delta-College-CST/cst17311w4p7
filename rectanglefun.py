# CST 173 - Delta College
# This program prompts for a rectangle length & width.  It then
# calculates and displays the rectangle area and perimeter

# Input rectangle length
def inputLength():
    len = float(input("==> Enter rectangle length (meters): "))
    return len

def inputWidth():
    wid  = float(input("==> Enter retangle width (meters): "))
    return wid

# Calculate area of a rectangle
def calcArea(len,wid):
    area = len * wid
    return area

# Calculate perimeter of a rectangle
def calcPerimeter(len,wid):
    perim = 2 * len + 2 * wid
    return perim

# Output
def outputResults(len,wid,area,perim):
    print("\n")
    print ("For rectangle dimensions",length,"meters X",width,"meters:")
    print ("  Perimeter:",perimeter,"meters")
    print ("  Area:",area,"square meters")
    
# ---------------------- MAINLINE ROUTINE ---------------------- #

# Input
length = inputLength()
width  = inputWidth()

# Calculations
area      = calcArea(length,width)
perimeter = calcPerimeter(length,width)

# Output
outputResults(length,width,area,perimeter)
