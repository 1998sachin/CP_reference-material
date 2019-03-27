# this calculates the factorial using tail recurion, it's equivalent to loop
def fact_tail_recursive(n,num):
	if n==1 or n==0:
		return num
	else:
		return fact_tail_recursive(n-1,n*num)

n=int(input())
print(fact_tail_recursive(n,1))

#BUT PYTHON DOEST NOT SUPPORT TAIL RECURSION