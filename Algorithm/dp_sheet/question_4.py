def find_initial(string) :
	count = 0
	for i in range(len(string)):
		if string[i] == 'R' :
			count += 1
	return count
	
def myfunction(string):
	R = find_initial(string)
	SUM = 0
	MAX = -1
	for i in range(len(string)) :
		if string[i] == 'R' :
			SUM = max(SUM - 1, -1)
		elif	string[i] =='K' :
			SUM = max(SUM + 1, 1)
		if SUM > MAX :
			MAX = SUM
	return R + MAX
t = int(input())
while t > 0 :
	string = list(input())
	print(myfunction(string))
	t -=1

		