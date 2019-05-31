x_read = open("john.txt","r")
x_write = open("johnboy.txt","w")
for words in x_read:
	print(words, file=x_write)
