cost = int(input("place item price here:"))
paid = int(input("place amount given here:"))
change = paid-cost
print("----------")
if (change/50)>=1:
	print("50s : ",int(change/50))
	print("----------")
if (change%50>0):
	if ((change%50)/20>=1):
		print("20s : ",int((change%50)/20))
		print("----------")
	if (((change%50)%20)/10)>=1:
		print("10s : ",int(((change%50)%20)/10))
		print("----------")
	if ((((change%50)%20)%10)/5>=1):
		print("5s : ",int(((change%50)%20)/5))
		print("----------")
	if (((((change%50)%20)%10)%5)/2>=1):
		print("2s : ",int(((((change%50)%20)%10)%5)/2))
		print("----------")
	if ((((((change%50)%20)%10)%5)%2)>=1):
		print("1s : ",int((((((change%50)%20)%10)%5)%2)))
		print("----------")






		
