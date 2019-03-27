alpha=[]
for i in range(1,27):
	alpha.append(str(i))

def check_and_print(arr):
	mystring=[]
	for i in range(len(arr)):
		if arr[i] in alpha:
			mystring.append(chr(int(arr[i])+96))
		else:
			return
	else:
		print("".join(mystring))

def myfunction(string, size):
	if size==1:
		return
	else:
		for i in range(0,len(string)-size+1):
			aux=string[0:i]
			aux+=["".join(string[i:i+size])]
			aux+=string[i+size:]
			#print(aux)
			check_and_print(aux)
	myfunction(string,size-1)

def first(string,size):
	check_and_print(string)
	myfunction(string,size)

first(['1','1','2','3'],2)