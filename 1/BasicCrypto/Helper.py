from math import gcd

"""
Not optimized implementation of Euler function computation.
"""
def eulerFunction(n):
	result = 1
	for i in range(2, n):
		if gcd(n, i) == 1:
			result += 1
	return result