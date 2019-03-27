#this is longest increasing subsequence problem from clrs using recursion
def LIS(arr,i,last):
	if i>=len(arr):
		return 0
	q=0
	for j in range(i,len(arr)):
		if last <arr[j]:
			q=max(q,1+LIS(arr,j+1,arr[j]))

	return q
arr=list(map(int,input().split(' ')))
print(LIS(arr,0,-100000))