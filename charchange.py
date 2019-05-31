x_read = open("john.txt","r")
x_write = open("piratejohn","w")
for words in x_read:
	for ch in words:
		if ch=="a":
			print("arrrrrr",file=x_write,end="")
		else:
			print(ch,file=x_write,end="")

