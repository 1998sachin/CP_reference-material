# this is longest increasing subsequence using bottom up approach, n^2 time complexity
def LIS(arr,n):
	aux=[1]*n 	# ith element contains the LIS from 0 to i index. 

	for i in range(1,n):		#starting from second element
		q=1					#min length of an LIS
		for j in range(0,i):
			if arr[i]>arr[j]:	#find the maximum LIS from 0 to i-1 index
				q=max(q, 1+aux[j])	
		aux[i]=q

	return max(aux)

arr=list(map(int,input().split(' ')))
print(LIS(arr,len(arr)))