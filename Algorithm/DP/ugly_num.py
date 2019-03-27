#Source is geeksforgeeks.com
def ugly_number(n):
	ugly_arr=[1]	# array to store ugly number sequence
	i2,i3,i5=0,0,0

	t=1	#loop variable
	while t<n:
		a=ugly_arr[i2]*2
		b=ugly_arr[i3]*3
		c=ugly_arr[i5]*5
		min_num=min(a,b,c)
		if min_num==a:	# These three if are not iefficient codes but essential to logic	
			i2+=1
		if min_num==b:
			i3+=1
		if min_num==c:
			i5+=1
		ugly_arr.append(min_num)
		t+=1
	#print(ugly_arr)
	return ugly_arr[n-1]
print(ugly_number(7))