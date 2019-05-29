def wordcount(message):
	word=1
	i=0
	while i<len(message):
		if message[i]==" ":
			word+=1
		i+=1
	return word

phrase=input('enter your phrase here:')

print("words:",wordcount(phrase))
