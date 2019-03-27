def get_spf():
	n = 10 ** 6
	spf = [1] * (n + 1)
	mark = [1] * (n + 1)
	for i in range(2, n + 1):
		if mark[i] == 1:
			spf[i] = i
			j = i * i
			while j <= n:
				mark[j] = 0
				if spf[j] == 1:
					spf[j] = i
				j += i 
	return spf