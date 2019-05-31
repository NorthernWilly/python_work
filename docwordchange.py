find=input("What word are you looking for?:")
replace=input("What would you like to replace it with?:")

f_read=open("john.txt","r")
f_write=open("johnjohn.txt","w")

for data in f_read:
	i=0
	while i<len(data):
		if data[i]==find[0]:
			if data[i:len(find)+i]==find:
				print(replace,end=" ",file=f_write)
				i+=len(find)-1
			else:
				print(data[i],end="",file=f_write)
		else:
			print(data[i],end="",file=f_write)
		i+=1

