import sys

salary = input("Enter monthly salary:  ")
print ("This is your salary", salary,)
print ("You will have", salary/50000, "that you can buy")
need = abs(50000-salary)
print ("You need", need, "to have 1 unit")
excess = abs(50000-(salary - 50000))
print ("You will need", excess, "to have 2 units") 
