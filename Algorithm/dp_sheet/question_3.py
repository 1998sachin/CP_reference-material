def myfunction(dp, arr) :
	for i in range(len(arr) -1, -1, -1) :
		dp[i] = max(dp[i+1], arr[i] + dp[i+2])
	return dp[0]

T = int(input())
t = T
while t > 0 :
	n = int(input())
	arr = list(map(int, input().split(' ')))
	dp = [0] * (len(arr) + 2)
	print("Case %d:"%(T - t + 1), myfunction(dp, arr))
	t -= 1