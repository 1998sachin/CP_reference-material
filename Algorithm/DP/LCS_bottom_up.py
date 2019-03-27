# LCS problem from clrs in Dynamic programming using bottom-up approach
def printing_LCS(b,X,i,j):
	if i==-1 or j==-1:
		return
	if b[i][j]=="1":
		printing_LCS(b,X,i-1,j-1)
		print(X[i],end=" ")
	elif b[i][j]=="2":
		printing_LCS(b,X,i,j-1)
	else:
		printing_LCS(b,X,i-1,j)

X=input().split(' ')	#first sequence
Y=input().split(' ')	#second sequence
m=len(X)
n=len(Y)
Table=[[-1 for x in range(n+1)] for x in range(m+1)]	#to store LCS 

b=[[0 for x in range(n)] for x in range(m)]	#for printing purpose

for i in range(0,m+1):	#setting the first row of table to 0
	Table[i][0]=0
for j in range(0,n+1):	#setting the first coloumn of table to 0
	Table[0][j]=0

for i in range(1,m+1):
	for j in range(1,n+1):		
		if X[i-1]==Y[j-1]:		#see the recursive solution
			Table[i][j]=1+Table[i-1][j-1]
			b[i-1][j-1]="1"
		elif Table[i][j-1]>=Table[i-1][j]:		#line upto line 31 to 36 can be written as Table[i][j]=max(Table[i-1][j],Table[i][j-1])
			Table[i][j]=Table[i][j-1]			#We are writing line 31 to 36 because we want to print the LCS (b table)
			b[i-1][j-1]="2"
		else:
			Table[i][j]=Table[i-1][j]
			b[i-1][j-1]="3"

printing_LCS(b,X,m-1,n-1)

