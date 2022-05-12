# Practise - Source - https://www.w3resource.com/python-exercises/lambda/index.php
# Even 
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = filter(lambda x : x%2 == 0,l)
print(list(is_even))
    
# Odd
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_odd = filter(lambda x : x%2 != 0,l)
print(list(is_odd))
    
#mapping 
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_square = map(lambda x : x**2,l)
print(list(is_square))
is_cube = map(lambda x : x**3,l)
print(list(is_cube))

# Adding two lists: 
l1 = [1, 2, 3]
l2 = [4, 5, 6]
final_lst = map(lambda x,y : x+y,l1,l2)
print(list(final_lst))

# Filter & Lambda : 
l = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
lst = filter(lambda x:(x%19 == 0 or x%13 == 0),l)
print(list(lst))

# Palindrome: 
l = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] 
print(l[0][0] == l[0][-1])
new = map(lambda x : (x[0][0:] == x[0][-1:]),l)
print(list(new))

# Palindrome (Solution2):
texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("\nList of palindromes:")
print(result) 

##Q8) extract year, month, date and time using Lambda
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

###Q10)to create Fibonacci series upto n using Lambda: Analysis in Copy

from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
print("Fibonacci series upto 2:")
print(fib_series(3))

###Q11) to find intersection of two given arrays using Lambda: 
##Desrired O/p : Intersection of the said arrays: [1, 2, 8, 9]
l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
new_lst = filter(lambda x: x  in l1,l2)
print("Intersection of the said arrays: ")
print(list(new_lst))

####Q12)Write a Python program to find all anagrams of a string in a given list of strings using lambda: 
###Orginal list of strings:
##['bcda', 'abce', 'cbda', 'cbea', 'adcb']
##Anagrams of 'abcd' in the above string:
##['bcda', 'cbda', 'adcb']
##Soln: 
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)

###Q13) to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))
print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))

###Q14) Write a Python program that sum the length of the names of a given list of names after removing the names that starts with a lowercase letter. 
##Use lambda function.
###soln: 
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print(sample_names)
print("Result:")
print(len(''.join(sample_names)))


### Qn: Write a lambda functn that take a list list1 as a parameter and multiplies each element of range(1,5) with each element of list1 using a list comprehension. 
### Soln: 
lam = lambda list1: [x * y for x in range(1, 5) for y in list1]
print(lam([1, 2]))

