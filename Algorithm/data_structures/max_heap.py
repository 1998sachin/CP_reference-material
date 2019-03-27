# heap and heap sort implementation


# index of left child
def left(i):
	return 2*i 


# index of right child
def right(i):
	return 2*i + 1


# swap function
def swap(arr, i, j):
	t = arr[i]
	arr[i] = arr[j]
	arr[j] = t 


# max_heapify maintains the max heap property
def max_heapify(arr, i):
	global heap_length
	
	l = left(i)
	r = right(i)

	if l < heap_length and arr[i] < arr[l]:
		largest = l
	else:
		largest = i 

	if r < heap_length and arr[largest] < arr[r]:
		largest = r 

	if largest != i:
		swap(arr, i, largest)
		max_heapify(arr, largest)


# for initial build up
def build_heap(arr):
	for i in range(len(arr) // 2, 0, -1):
		max_heapify(arr, i)


# heap sort function
def heap_sort(arr):
	global heap_length
	build_heap(arr)
	for i in range(len(arr)-1, 1, -1):
		swap(arr, i, 1)
		heap_length -= 1
		max_heapify(arr, 1)


# main starts
arr = ['empty', 2, 3, 4, 1, 7, 12, 8]
heap_length = len(arr)
heap_sort(arr)
print(arr[1:])
