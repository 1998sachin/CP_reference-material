# this is longest increasing subsequence using bottom up approach, nlog(n) time complexity
def binary_search(start, last, arr, item):	#binary search function
	if start>=last:
		return start
	mid=int((start+last)/2)
	if arr[mid]==item:
		return mid 
	else:
		if arr[mid]>item :
			a= binary_search(start,mid-1,arr, item)
		elif arr[mid]<item:
			a= binary_search(mid+1,last, arr, item)
		if  a<len(arr) and arr[a]<item:
			return a+1
		else:
				return a

def LIS(arr,n):
	
	C=[] #ith element contains the minimum of the last element if LIS of length i+1
	C.append(arr[0])
	last=0 #it marks the index of last element of C
	for  i in range(1,n):
		if arr[i]<=C[0]:		#if arr[i] is smallest element
			C[0]=arr[i]

		elif arr[i]>C[last]:
			last+=1
			C.append(arr[i])
		else:
			k=binary_search(1,last,C,arr[i])	#return index k such that arr[k-1]<arr[i]<arr[k]
			C[k]=arr[i]
	
	return len(C)

arr=list(map(int,input().split(' ')))
print(LIS(arr,len(arr)))