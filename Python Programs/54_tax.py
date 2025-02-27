salary=int(input("Enter the salary :"))
tax=salary*0.10
provident_fund=salary*0.12
deductions=tax+provident_fund
net_salary=salary-deductions
print("The net salary of the employee is :",net_salary)