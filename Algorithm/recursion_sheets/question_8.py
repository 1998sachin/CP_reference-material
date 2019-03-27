def myfunction(string,array,k):
	if len(array)==k:
		print("".join(array))
		return
		
	for i in range(len(string)):
		aux_2=array[:]
		aux_2.append(string[i])
		myfunction(string,aux_2,k)

myfunction(['a','b','c','d'],[],2)
