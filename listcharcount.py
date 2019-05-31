try:

	a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	i=0
	msg = input("enter any letters:").upper()

	while i<len(msg):
		a[(ord(msg[i]))-65]+=1
		i+=1

	x=0
	while x<=25:
		if a[x]>0:
			print(chr(x+65)," = ",a[x])
		x+=1
except IndexError:
	print("I SAID ENTER LETTERS YOU MUPPET! STOP ENTERING NUMBERS AND/OR SPECIAL CHARACTERS!")
