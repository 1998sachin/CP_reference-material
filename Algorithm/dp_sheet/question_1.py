def first_char(string) :
	return string[0]
def two_char(string) :
	if len(string) > 1 :
		if string[0] == 0:
			return 0
		else:
			return string[0] * 10 + string[1]
	else :
		return 0

def check(num) :
	if num > 0 and num < 27 :
		return 1
	else :
		return 0

def myfunction(string) :
	global count
	if string == [] :
		count += 1
		return 
	else :
		if check(first_char(string)) :
			myfunction(string[1:])
		else :
			return 
		if check(two_char(string)) :
			myfunction(string[2:])
		else:
			return
def using_dp(string) :
	global dp 
	dp[len(string)] = 1
	dp[len(string) + 1] = 1
	for i in range(len(string) - 1, -1, -1) :
		sum_first = 0; sum_second = 0
		if check(first_char(string[i:])) :
			sum_first = dp[i + 1]
		if check(two_char(string[i:])) :
			sum_second = dp[i + 2]
		dp[i] = sum_first + sum_second
	return dp[0]
		
string = list(map(int,input()))
count = 0
dp = [0] * (len(string) + 2)
myfunction(string)
print(count)
print(using_dp(string))
