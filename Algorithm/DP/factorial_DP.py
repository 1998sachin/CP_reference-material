#this uses dynamic programming approach Top-down
def fact_dp(n,arr):
	if n<len(arr):
		return arr[n]
	else:
		result= n*fact_dp(n-1,arr)
		arr.append(result)
		return result

arr=[1,1]
n=int(input())
print(fact_dp(n,arr))