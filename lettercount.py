msg = input("enter your message").upper()

def count(letter,what):
	i=0
	found=0
	while i<len(msg):
		if msg[i]==what:
			found+=1
		i+=1
	if found>0:
		print(what, "= ",found)

char = 65
while char<=90:
	count(msg,chr(char))
	char+=1

