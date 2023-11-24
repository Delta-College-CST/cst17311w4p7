# This program utilizes the LinearFunction class to analyze
# lines

from LinearFunction import LinearFunction

# Define and initialize object:  y = 3x + 4
line = LinearFunction(3.0, 4.0) 

print("f(5) = ",line.calcYfromX(5.0))        # Find y when x is 5

print("x-intercept ",line.getXintercept())   # Find x-intercept

