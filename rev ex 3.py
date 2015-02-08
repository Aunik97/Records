class Employee():
    def __init__(self, name, number = None, hours_per_week = None, hourly_rate = None):
        self.name = name
        self.number = number
        self.hours_per_week = hours_per_week
        self.hourly_rate = hourly_rate

    def __repr__(self):
        return "{0} | {1} | {2} | {3} |".format(self.name, self.number, self.hours_per_week,self.hourly_rate)

    def __str__(self):
        return "Nothing"



def row(s):
    print("*{0:<30}*".format(s))
#name = input("name of employee")
#e = Employee(name)
#e.number, e.hours_per_week, e.hourly_rate = input("number"), input("hours per week"), input("pay rate")
print("PAY SLIP GENERATOR")

name = input("please enter the name of employee: ")
e = Employee(name)
e.number = input("please enter the employee's number")
e.hours_per_week = input("please eneter the hours worked by this employee")
e.hourly_rate = input("please enter the employee's rate of pay")
print("\n\n")
row("*" * 30)
row("Pay Slip")
row(" ")
row("Name: " + e.name)
row("Employee Number: " + e.number)
row("Hours Worked: " + e.hours_per_week)
row("Rate Of Pay: " + e.hourly_rate)
row(" ")
row("Total Pay: £{0:.2f}".format(float(e.hours_per_week) * float(e.hourly_rate)))
row("*" * 30)
