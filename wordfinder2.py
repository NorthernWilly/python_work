msg=input("enter your sentence?:")
search=input("word you wish to count:")
i=0
word=""
count=0
while i<len(msg):
	if msg[i]==" ":
		if search==word:
			count=count+1
		word=""
		i=i+1
	word=word+msg[i]
	i=i+1
print("you have",count,search,"(s) in your sentence")

