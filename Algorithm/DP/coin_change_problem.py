# this is 'The Coin Change Problem' using dynamic programming
# source hackerrank
def getways(SUM, index) :
	global dp 
	global d
	global size_of_d

	if SUM < 0 or index >= size_of_d:
		return 0
	elif SUM == 0 :
		return 1
	elif dp[index][SUM]!=-1 :
		return dp[index][SUM]
	else :
		count = getways(SUM - d[index], index)
		count += getways(SUM, index + 1)
		dp[index][SUM] = count
		return count

SUM = int(input())
size_of_d = int(input())	#size of denomination array
d = list(map(int, input().split(' ')))
dp = [[-1 for x in range(SUM+1)] for y in range(size_of_d)] 
print(getways(SUM, 0))

