# This program processes payroll for hourly workers

from Employee import Employee

print("NAME    HOURS    PAY")          # Reporting heading

datafile = open("workerdata.txt", "r") # Open file for reading

# Initialize pay
totalPay = 0

# Perform file processing loop until end
for line in datafile:

    # Read one line of data - one worker
    hoursStr, rateStr = line.split(",")

    # Convert numeric strings to numbers
    hours = float(hoursStr)
    rate  = float(rateStr)

    worker = Employee(hours,rate)

    # Determine pay, add to total, and write line of output
    pay     = worker.calcGrossPay()
    totalPay += pay
    print (worker.summaryReport() + "\n")

# Write total as report summary
print ("TOTAL        $%7.2f" % (totalPay))


