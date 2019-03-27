def all_subset(SET,current_buffer):
	print(current_buffer)
	
	for i in range(len(SET)):
		#subset.append(current_buffer+[SET[i]])
		aux=SET[i:]
		aux.remove(SET[i])
		all_subset(aux,current_buffer+[SET[i]])

	

all_subset([1,2,3,4],[])