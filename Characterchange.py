alpha = input("enter any letter for an endless magical journey:")

if ord(alpha)>=65 and ord(alpha)<=90:
	print("oh isnt it wonderful...",chr(ord(alpha)+32))
else:
	if ord(alpha)>=97 and ord(alpha)<=122:
		print("Yep, that's right, its magic...",chr(ord(alpha)-32))
	else:
		print("I said a letter you muppet, how do you even think magic works!?")

