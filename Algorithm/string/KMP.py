'''input
ghghghgxghghghg
'''
# KMP prefix structure
from sys import stdin


def prefix_calculator(string):
	p = [0] * len(string)
	j = 0
	for i in range(1, len(string)):
		while j > 0 and string[i] != string[j]:
			j = p[j - 1]

		if string[i] == string[j]:
			j += 1
		p[i] = j
		
	return p


# main starts
string = stdin.readline().strip()
p = prefix_calculator(string)
