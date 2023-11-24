# This program calculates and sums payroll for two hourly workers.

from Employee import Employee

# Prompt for worker input. Define and initialize objects
hoursWorked = float(input("Worker1: Hours worked: "))
payRate     = float(input("Worker1: Pay rate: "))
worker1 = Employee(hoursWorked, payRate)

hoursWorked = float(input("Worker2: Hours worked: "))
payRate     = float(input("Worker2: Pay rate: "))
worker2 = Employee(hoursWorked, payRate)

# Calculate and sum gross pay for both workers
totalPayroll = worker1.calcGrossPay() + worker2.calcGrossPay()

# Report payroll summary
print("\n\n")
print ("PAYROLL")
print()
print(worker1.summaryReport())
print()
print(worker2.summaryReport())
print()
print("Total: $%7.2f" % (totalPayroll))
