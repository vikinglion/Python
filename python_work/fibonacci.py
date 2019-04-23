#!usr/bin/env python
#coding=utf-8


#recursion
'''
def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):	
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
'''

'''
#iteration
def fibonacci(n):
	n1 = 0
	n2 = 1
	n3 = n
	i = 0
	while (i <= n):
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		i += 1
	return n3
'''

#tail recursion
def fibonacci(first, second, n):
	if (n<2):
		return n
	if (n == 2):
		return first+second
	return fibonacci(second, first+second, n-1)

	

def product_fibonacci(prod):
	n = 0
	while 1:
		arr1 = fibonacci(n)
		arr2 = fibonacci(n+1)
		product = arr1 * arr2
		result = [arr1, arr2]
		if (prod == product):
			result.append(True)
			return result
		elif (product > prod):
			result.append(False)
			return result
		print(product)
		n += 1
		
#´óÀÐ´úÂë		
'''
def productFib(prod):
  a = 0
  b = 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
'''

print(fibonacci(0, 1, 5))
#print(product_fibonacci(5))
	
