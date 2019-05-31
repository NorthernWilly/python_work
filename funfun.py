def sub(x,y):
	c=x-y
	print("result of subraction is:",c)

def add(x,y):
	c=x+y
	print("the result of addition is:",c)

def ops(f,x,y):
	f(x,y)

x=int(input("put your 'x' value here:"))
y=int(input("put your 'y' value here:"))

ops(add,x,y)

ops(sub,x,y)