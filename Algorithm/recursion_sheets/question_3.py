def binary_search(start, last, arr, item):
	if start<=last:
		mid=int((start+last)/2)
		if arr[mid]==item:
			return mid 
		else:
			if arr[mid]>item :
				return  binary_search(start,mid-1,arr, item)
			elif arr[mid]<item:
				return binary_search(mid+1,last, arr, item)
			
	else:
		return -1

arr=[1,2,4,5,6,7]
print(binary_search(0,len(arr),arr,5))