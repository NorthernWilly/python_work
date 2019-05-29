def tax(salary):
	if salary > 1500:
		t=salary*21/100
	else:
		t=salary * 15/100

	return t

salary1=int(input("enter your salary:"))

print("your tax:",tax(salary1))
print("your net salary:",(salary1-tax(salary1)))
