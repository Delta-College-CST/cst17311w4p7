# This program performs a statistical analysis of a
# set of positive integer values.

from Statistics import Statistics 

stats = Statistics("data.txt")   # Construct statistics object

# Perform calculations and write
average = stats.calcAverage()
print("Average: %6.2f" % (average))

maxValue = stats.getMax()
print("Maximum:",maxValue)

minValue = stats.getMin()
print("Minimum:",minValue)
