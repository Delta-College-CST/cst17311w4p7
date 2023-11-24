# This class manages a statistical dataset of a
# set of positive integer values.  Its constructor reads the data from
# an external file and stores it in an array.  The specific
# statistical operations are managed via functions.

class Statistics:
    
    # Constructor
    def __init__(self, filename):
        self.datalist = []
        datafile = open(filename, "r")
        for inputStrItem in datafile:
            element = int(inputStrItem)
            self.datalist.append(element)
        datafile.close()

    # Calculate average value in a list of integers
    def calcAverage(self):
        sum = 0
        for item in self.datalist:
             sum += item
        ave = sum / len(self.datalist)
        return ave

    # Determine largest value in list of integers
    def getMax(self):
        max = -99999999
        for item in self.datalist:
             if item > max:
                 max = item
        return max

    # Determine largest value in list of integers
    def getMin(self):
        min = 99999999
        for item in self.datalist:
             if item < min:
                 min = item
        return min

