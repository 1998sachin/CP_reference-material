#coding ninjas problem min steps to one (Dynamic programming)

def myfunction_1(n):		#recursive (give segmentation fault for larger n)
	if n == 1 :
		return 0 
	if dp[n] != 0 :
		return dp[n]
	else :
		var = var3 = 1 + myfunction_1(n-1)
		if n % 3 == 0 :
			var = min(var, 1 + myfunction_1(int(n/3)))
		
		if n % 2 == 0 :
			var = min(var, 1 + myfunction_1(int(n/2)))
		
		dp[n] = var
		return var

def myfunction_2(n):		#better solution 
	for i in range(2, n+1):
		var = 1 + dp[i-1]

		if i % 2 == 0:
			var = min(var, 1 + dp[int(i/2)])
		if i % 3 == 0:
			var = min(var, 1 + dp[int(i/3)])
		dp[i]=var
	
	return dp[n]
		
n = int(input())
dp = [0] * (n + 1)
#print(myfunction_1(n))
print(myfunction_2(n))