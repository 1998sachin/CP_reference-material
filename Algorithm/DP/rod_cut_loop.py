# rod cutting prooblem from clrs in Dynamic programming using bottom-up or loop approach
def rod_cut(p,n):	#recursive function definition
	r=[0]			
	for i in range (1,n+1):
		k=-10000
		for j in range(1,i+1):
			k=max(k,p[j-1]+r[i-j])
		r.append(k)
	return r[n]



n=int(input()) #size of the rod
#p=list(map(int,input().split(' '))) # size vs price table... index 0 means length 1 and index n means lenth n+1
p=[1,5,8,9,10,17,17,20,24,30]	#this is taken for checking purpose from clrs
print(rod_cut(p,n))
