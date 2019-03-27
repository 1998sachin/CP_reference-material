def fib(n):
	mem=[0]*n 
	mem[0]=1
	mem[1]=1
	for i in range(0,n-2):
		mem[i+2]=mem[i]+mem[i+1]
	else:
		return mem[n-1]

print(fib(40000))