def LCS(X,Y,i,j):
	if i+1==0 or j+1==0:
		return 0
	else:
		if X[i]==Y[j]:
			return 1+LCS(X,Y,i-1,j-1)
		else:
			return max(LCS(X,Y,i-1,j),LCS(X,Y,i,j-1))

X=input().split(' ')	#first sequence
Y=input().split(' ')	#second sequence
m=len(X)
n=len(Y)
print(LCS(X,Y,m-1,n-1))