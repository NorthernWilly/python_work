def ops(day):
	if day==1:
		def fun(a,b):
			c=a+b
			print("the result of adding is:",c)

	if day ==2:
		def fun(a,b):
			c=a-b 
			print("The result of subtracting is:",c)
	return fun

bill=ops(1)
bill(9,5)

bill=ops(2)
bill(9,5)

