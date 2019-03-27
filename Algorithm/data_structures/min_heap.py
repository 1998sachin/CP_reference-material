# min heap but there are some errors
def left(arr, i) :
	return 2*i

def right(arr, i) :
	return 2*i + 1

def parent(arr, i) :
	return int(i/2)

def swap(arr, i, j) :
	t = arr[i]
	arr[i] = arr[j]
	arr[j] = t 

def min_heapify(arr, i) :
	global heap_length
	l = left(arr, i)
	r = right(arr, i)

	if l < heap_length  and arr[i] > arr[l] :
		smallest = l
	else :
		smallest = i 

	if r < heap_length and arr[smallest] > arr[r] :
		smallest = r 

	if smallest != i :
		swap(arr, i, smallest)
		min_heapify(arr, smallest)

def build_min_heap(arr) :
	for i in range (int(len(arr)/2), 0, -1) :
		min_heapify(arr, i)

def extract_min(arr) :
	global heap_length
	MIN = arr[1]
	swap(arr, 1, heap_length-1)
	heap_length -= 1 
	min_heapify(arr, 1)
	del arr[-1]
	return MIN 

def insert(arr, element) :
	global heap_length
	arr.append(element)
	heap_length += 1
	j = heap_length - 1
	while parent(arr, j) > 0 and parent(arr, j) > arr[j] :
		swap(arr, j, parent(arr, j))
		j = parent(arr, j)


arr = ['null']
heap_length = len(arr)
build_min_heap(arr)
print(arr[1:])
insert(arr, -1)
print(arr[1:])