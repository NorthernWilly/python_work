msg=input("enter your sentence?:")
search=input("word you wish to change:")
newword=input("word you want it to be:")
i=0
word=""
count=0
newmsg=""
while i<len(msg):
	if msg[i]==" ":
		if search==word:
			word=newword
			newmsg+=word+" "
			word=""
		else:
			newmsg+=word+" "
			word=""
	else:
		if i==(len(msg)-1):
			word=word+msg[i]
			if search==word:
				word=newword
				newmsg+=word+" "
		else:
			word=word+msg[i]
	i=i+1


print(newmsg)

