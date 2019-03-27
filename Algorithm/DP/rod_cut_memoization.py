# rod cutting prooblem from clrs in Dynamic programming using memoization method
def rod_cut(p,n,r):
	if n==0:
		return n
	else:
		if n<len(r):
			return r[n]
		else:
			k=-100000
			for i in range (len(r),n+1):
				k=max(k, p[i-1]+rod_cut(p,n-i,r))
			r.append(k)
			return r[-1]		


n=int(input()) #size of the rod
#p=list(map(int,input().split(' '))) # size vs price table... index 0 means length 1 and index n means lenth n+1
p=[1,5,8,9,10,17,17,20,24,30]	#this is taken for checking purpose from clrs
r=[0]	#this is the revenue array...it grows dynamically
print(rod_cut(p,n,r))
