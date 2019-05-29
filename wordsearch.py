
msg=input("Enter your sentence:")
option=input("would you like to count a letter?")
while option=="yes":
	letter=input("what letter do you wish to count?:")
	i=0
	count=0
	while i<len(msg):
		if msg[i]==letter:
			count=count+1
		i=i+1
	print("Your sentence has",count, letter,"'s")
	option=input("would you like to count another letter:")
print("Thankyou for using this program")
