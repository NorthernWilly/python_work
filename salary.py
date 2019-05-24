name = input("ENTER YOUR NAME:")
salary = int(input("ENTER YOUR SALARY:"))

if salary>2000:
	tax = salary*25/100
else:
	tax = salary*15/100

netsalary = salary - tax

print("Your Name:",name)
print("Salary:",salary)
print("Tax:",tax)
print("Your Take-home Pay:",netsalary)
print("-----------------------------------------")
