# using dynamic programming
def myfunction_1(SUM):	#dp solution
	global dp 
	if SUM < 0 :
		return 0
	if SUM == 0 :
		return 1
	if dp[SUM] != -1 :
		return dp[SUM]
	count = myfunction_1(SUM -1)
	count += myfunction_1(SUM -2)
	count += myfunction_1(SUM -3)	
	dp[SUM] = count
	return count

def myfunction_2(SUM,count):	#recursive solution
	if SUM==0:
		pass
	else:
		for i in range(1,4):
			if SUM-i ==0:
				count+=1; break;
			elif SUM-i>0:
				count=myfunction_2(SUM-i,count)
			else:
				continue
	return count

n = int(input())
dp = [-1] * (n + 1)
print(myfunction_1(n))
print(myfunction_2(n, 0))