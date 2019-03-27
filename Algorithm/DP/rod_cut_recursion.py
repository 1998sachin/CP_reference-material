# rod cutting prooblem from clrs in Dynamic programming using simple recursion
def rod_cut(p,n):	#recursive function definition
	if n==0:
		return 0
	k=-1000000
	for i in range(1,n+1):
		k=max(k,p[i-1]+rod_cut(p,n-i))

	return k

n=int(input()) #size of the rod
#p=list(map(int,input().split(' '))) # size vs price table... index 0 means length 1 and index n means lenth n+1
p=[1,5,8,9,10,17,17,20,24,30]	#this is taken for checking purpose from clrs
print(rod_cut(p,n))
