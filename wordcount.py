word = 0 
msg = input("enter message:")
i = 0

while i<len(msg):
	if msg[i]==(" "):
		word = word+1
	i=i+1
print ("message has",(word+1),"word(s)")

