# This class manages the information for one hourly employee.

class Employee:
    
    BASE_HOURS = 40.0
    
    # Constructor - set attributes hours and payrate 
    def __init__(self, hours , rate):
        self.hoursworked = hours
        self.payrate = rate

    # Calculate gross pay for week
    def calcGrossPay(self):
        if self.hoursworked <= self.BASE_HOURS:
            pay = self.hoursworked * self.payrate
        else:
            pay = self.hoursworked * self.BASE_HOURS +    \
                 (self.hoursworked - self.BASE_HOURS) * 1.5 * self.payrate
        return pay

    # Method creates summary for this worker - returns as string
    def summaryReport(self):
        reportOut = ""
        reportOut += "Pay rate:    $%6.2f per hour" % (self.payrate)
        reportOut += "\n"
        reportOut += "Hours Worked: %4d hours" % (self.hoursworked)
        reportOut += "\n"
        reportOut += "Paycheck: $%7.2f" % (self.calcGrossPay())
        return reportOut
       

