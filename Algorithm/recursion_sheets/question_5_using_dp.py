def myfunction(index,arr, SUM,dp):
	if SUM==0:
		return 1
	elif len(arr)==0 or SUM<0:
		return 0

	elif dp[index][SUM-1]!=-1:
		return dp[index][SUM-1]
	else:
		first=arr[0]
		var1= myfunction(index+1,arr[1:],SUM-first,dp)
		var2= myfunction(index+1,arr[1:],SUM,dp)
		
		dp[index][SUM-1]=var1+var2

		return var1+var2

arr=[5,1,3,3,7,4,2,3,3,1,4,3,3,52,3,1,5,1,4,1,3,1,4,1,4,6,1,1,1,1,1,4,5,6,7,8,9,9,1,2,3,4,5,6,7,8,8]
k=10
dp=[[-1 for x in range(k)] for y in range(len(arr))] 
print(myfunction(0,arr,k,dp))
print(dp)