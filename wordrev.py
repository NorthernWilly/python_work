def reverse(sound):
	a = len(sound)-1
	reverseword = ""
	while a>=0:
		reverseword+=sound[a]
		a-=1
	return reverseword


msg = input("Enter Message:")
word=""
i=0
newmsg = ""

while i<len(msg):
	if msg[i]==" ":
		newmsg+=(reverse(word))+" "
		word=""
	else:
		if i == (len(msg)-1):
			word=word+msg[i]
			newmsg+=(reverse(word))
		else:
			word=word+msg[i]
	i=i+1
print(newmsg)


