def fib(n):
	if len(mem)>=n:
		return mem[n-1]
	else:
		sum=fib(n-1)+fib(n-2)
		mem.append(sum)
		return sum

mem=[1,1]

print(fib(2))
