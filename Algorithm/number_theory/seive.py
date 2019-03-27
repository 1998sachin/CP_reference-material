def get_prime():
	n = 10 ** 6
	seive = [1] * (n + 1)
	for i in range(2, n + 1):
		if seive[i] == 1:
			j = i * i
			while j <= n:
				seive[j] = 0
				j += i

	primes = []
	for i in range(2, n + 1):
		if seive[i]:
			primes.append(i)
	return primes