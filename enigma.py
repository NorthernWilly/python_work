def change(message):
	i=0
	word=""
	while i<len(msg):
		if ord(msg[i])>=65 and ord(msg[i])<=90:
			letter=chr(ord(msg[i])+32)
			word=word+letter
		else:
			if ord(msg[i])>=97 and ord(msg[i])<=122:
				letter=chr(ord(msg[i])-32)
				word=word+letter
			else:
				if ord(msg[i])==32:
					word=word+msg[i]
				else:
					if ord(msg[i])>=48 and ord(msg[i])<=57:
						letter=int(msg[i])*2
						word=word+str(letter)
					else:
						letter=chr(ord(msg[i])+1)
						word=word+letter
		i+=1
	print(word)

msg=input("enter your secret message, do it now:")

change(msg)
