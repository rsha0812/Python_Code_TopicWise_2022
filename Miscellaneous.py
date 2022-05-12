#### Genrator : 
# def even(x):
#       while(x!=0):
#           if x%2==0:
#                  yield x
#           x-=1

# for i in even(8): 
#      print(i)

# #### Iterator : 
# s = {1,2}
# i = iter(s)
# a = next(i)
# print(a)
# b = next(i)
# print(b)
# c = next(i)
# print(c)


##### Recursion Limit : 
## Method1: 
# def cursing(depth): 
# 	try: 
# 		cursing(depth+1) ## actually recursing 
# 	except RuntimeError as RE: 
# 		print('I recursed {} times!'.format(depth))

# cursing(0) ## Output : I recursed 998 times!

# ## Method2: 
# import sys
# sys.setrecursionlimit(100)
# cursing(0)

###### Recursive Lambda Function: 
lambda_func = lambda i:1 if i == 0 else i*lambda_func(i-1)
print(lambda_func(4)) ## 24

###### Recursive Function: 
'''
A Recursive Function is a function that calls itself in its definition.'''
 
def factorial(n): 
	if n==0:  
		return 1 
	else: 
		return n * factorial(n-1)
print(factorial(4)) ## 24


