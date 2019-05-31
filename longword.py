
msg = input("Enter Message:")
word=""
i=0
longest=""
justaslong=""
while i<len(msg):
	if msg[i]==" ":
		if len(word)>len(longest):
			longest=word	
		if len(word)==len(longest):
			justaslong=word
		word=""
	else:
		if i==(len(msg)-1):
			word=word+msg[i]
			if len(word)>len(longest):
				longest=word
			if len(word)==len(longest):
				justaslong=word
		else:
			word=word+msg[i]
	i=i+1
print(longest)
print(justaslong)