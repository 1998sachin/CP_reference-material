def binary_search(start, last, arr, item):
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
		
arr=[2,4,6,10,15]

while True:
	n=int(input())
	print(binary_search(0,len(arr)-1,arr,n))