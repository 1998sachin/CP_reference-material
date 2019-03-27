#assumed all positive numbers
#ask the doubt for negative numbers 
def print_subset_sum(SET,SUM, sum_set):
	if SUM==0:
		return
	for i in range(len(SET)):
		if SET[i]==SUM:
			print(sum_set+[SET[i]])
		elif SET[i]<SUM:
			aux=SET[i:]
			aux.remove(SET[i])
			print_subset_sum(aux,SUM-SET[i],sum_set+[SET[i]])

print_subset_sum([5 ,12, 3, 17, 1, 18, 15, 3, 17],6,[])