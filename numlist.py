numbers=[]


while True:
	num = int(input("enter any number and keep on going! if you want to stop enter '0'"))
	if num==0:
		break
	else:
		numbers.append(num)

highest = numbers[0]
i=1
while i<len(numbers):
	if numbers[i]>highest:
		highest=numbers[i]
	i=i+1

print("the highest is ",highest)