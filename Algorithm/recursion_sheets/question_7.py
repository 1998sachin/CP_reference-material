def permutation(string,array):
	if string==[]:
		print("".join(array))
		return

	else:
		for i in range(len(string)):
			aux=array[0:]
			aux.append(string[i])
			aux_2=string[0:]
			aux_2.remove(string[i])
			permutation(aux_2,aux)	

permutation(['a','b','c','d'],[])