# CST 173 - Delta College
# This program prompts for a rectangle length & width.  It then
# calculates and displays the rectangle area and perimeter

# Input
length = float(input("==> Enter rectangle length (meters): "))
width  = float(input("==> Enter retangle width (meters): "))

# Calculate area and perimter of a rectangle
area      = length * width
perimeter = 2 * length + 2 * width

# Output
print("\n")
print ("For rectangle dimensions",length,"meters X",width,"meters:")
print ("  Perimeter:",perimeter,"meters")
print ("  Area:",area,"square meters")
