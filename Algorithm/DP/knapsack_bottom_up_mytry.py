#Its 0-1 knapsack problem bottom-up solution. This is my solution
def knapsack(w,v,k,n):	#this is knapsack function. It accepts 4 arguments. weight list(w),cost list(v),max weight(k),number of items(n).
	arr=[[0,0]]		#contains weight(index 0) and maximum cost(index 1) for corresponding weight.
	aux=[]			#contains weight and cost of cross between arr and a new item from item(weight and cost).(includes new item weight and cost)

	for i in range(0,n):
		if w[i]<=k:
			aux.append([w[i],v[i]])		#new item appended
			for j in range(0,len(arr)):		#creating a cross
				if arr[j][0]+w[i]<=k:		
					aux.append([arr[j][0]+w[i],arr[j][1]+v[i]])

			arr=merge(arr,aux)		#merges arr and aux.
			aux=[]					#aux become empty to repeat cycle(cross).

	maximum=0
	for i in range(len(arr)):		#finding maximum based on cost(index 1)
		maximum=max(maximum,arr[i][1])
	
	return maximum

def merge(arr,aux):		#it merges arr and aux
	i=0; j=0
	new=[]			#merged list
	while i<len(arr) and j<len(aux):
		if arr[i][0]<aux[j][0]:
			new.append(arr[i])
			i+=1
		elif arr[i][0]>aux[j][0]:
			new.append(aux[j])
			j+=1
		else:
			new.append([arr[i][0],max(arr[i][1],aux[j][1])])	#if weight arr[i]==weight aux[j](index 0), new[][1] stores the maximum cost between arr[i][1] and aux[j][1].
			i+=1;j+=1

	if i<len(arr):			#append remaining list
		while i<len(arr):
			new.append(arr[i])
			i+=1
	elif j<len(aux):
		while j<len(aux):
			new.append(aux[j])
			j+=1
	return new

nk=list(map(int,input().strip().split()))	#stores the n and k in a list
n=nk[0]		#number of items 
k=nk[1]		#maximum weight
v=list(map(int,input().strip().split()))	#list containing cost of items
w=list(map(int,input().strip().split()))	#list containing weight of items
print(knapsack(w,v,k,n))