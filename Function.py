### Function: https://www.w3resource.com/python-exercises/python-functions-exercises.php

#### Udemy: 

## Qn: Write a function that takes one positional arg x and a variable-length tuple parameter and return result of multiplying x with 2nd element of Tuple.
### Soln: 
def my_func(x,*args): 
    return x * args[1]
result = my_func(5, 10, 20, 30, 50)
print(result)

## Same Qn using Dict(kwargs): 
## Soln1: 
def my_func(x,**kwargs):
    return x * max(kwargs.values())
result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
print(result)

## Soln2: 
def my_func(x, **kwargs):
    return x * sorted(kwargs.values())[-1]
result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
print(result)

## Qn: Functn using Global Variable. 
var = 10
def my_func(x):
    global var 
    return x * var
print(my_func(20))

## Qn: Changing Global variable value by calling it as local variable. 
### Soln: 
var = 10
def my_func(x):
    var = 5
    print(x * var)
my_func(20)

## Qn: Importing pi Module from Maths and format output so that it will have only 4 digits after decimal(.).
### Soln: 
from math import pi
print("%.4f" % pi)

### Q1) Write a Python function to find the Max of three numbers.
#### Soln: 
def max_num(x,y,z): 
    if x>y and x>z: 
        print("{0} is Largest Number".format(x))
    elif y>x and y>z: 
        print("{0} is Largest Number".format(y))
    else: 
        print("{0} is Largest Number".format(z))
max_num(4,3,2)
max_num(14,33,2)
max_num(4,3,22)

### Q2) Write a Python function to sum all the numbers in a list.
#### Soln: 
def sum_lst(lst): 
    sum = 0 
    for i in lst: 
        sum += i
    return sum
print(sum([1,2,3,4]))
print(sum([1,12,3,4]))

### Q3) Write a Python function to multiply all the numbers in a list.
#### Soln: 
def mul_lst(lst): 
    mul = 1
    for i in lst: 
        mul = i * mul 
    return mul 
print(mul_lst([1,2,3]))


### Q4) Write a Python program to reverse a string.
#### Soln: 
def rev_string(str1): 
    l = len(str1)
    new_str = ''
    while l>0: 
        new_str = new_str + str1[l-1]
        l = l-1
    return new_str
print(rev_string("1234abcd"))


### Q5) Write a Python function to calculate the factorial of a number (a non-negative integer). 
##The function accepts the number as an argument
#### Soln: 
def fact(n): 
    if n==1 or n==0: 
        return 1
    else: 
        return n * fact(n-1)
print(fact(3))
print(fact(4))
print(fact(5))


### Q6) Write a Python function to check whether a number falls in a given range.
#### Soln: 
def num_check(n): 
    if n in range(0,25): 
        print("{0} falls in given range".format(n))
    else: 
        print("{0} not in given range".format(n))
    return n 
num_check(13)
num_check(33)

### Q7) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
#### Soln: 
def letter_count(str1): 
    u =0 
    l =0
    for i in str1: 
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        else: 
            pass 
    print("The Original String: ",str1)
    print("No. of Upper Case Character: ",u)
    print("No. of Lower Case Character: ",l)
(letter_count('The quick Brow Fox'))

### Q8) Write a Python function that takes a list and returns a new list with unique elements of the first list.
#### Soln: 
def unique_ele(lst): 
    new_lst = []
    for i in lst: 
        if i not in new_lst: 
            new_lst.append(i)
    return new_lst
print(unique_ele([1,2,3,3,3,3,4,5]))

### Function to remove Duplicate using List Comprehension: 
def my_func(x):
    lst = []
    [lst.append(i) for i in x if i not in lst]
    return sorted(lst) ## Sorting List in asc order 
    
result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)

### Soln2: 
def my_func(x):
    lst = []
    [lst.append(i) for i in x if i not in lst]
    return sorted(lst)
    
result = my_func([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)


### Q9) Write a Python function that takes a number as a parameter and check the number is prime or not.
#### Soln: 
def prime_number(n): 
    if n==1:
        return False 
    elif n ==2: 
        return True 
    else: 
        for i in range(2,n): 
            if (n%i == 0): 
                return False
        return True
print(prime_number(2))
print(prime_number(21))
print(prime_number(13))


### Q10) Write a Python program to print the even numbers from a given list.
#### Soln: 
def even_num(lst):
    even_lst = []
    for i in lst:
        if i%2 == 0: 
            even_lst.append(i)
    return even_lst
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


### Q11) Write a Python function to check whether a number is perfect or not.
#### Soln: 
def perfect_number(n): 
    sum = 0
    for i in range(1,n): 
        if(n%i == 0): 
            sum+= i
    return sum == n 
print(perfect_number(28))
     
### Q12) Write a Python function that checks whether a passed string is palindrome or not
#### Soln: 
def palindrome(word): 
    rev = ""
    i = len(word)-1
    while i>=0:
        rev = rev + word[i]
        i = i-1
    return word == rev 
print(palindrome("madam"))   


### Q13) Write a Python function that prints out the first n rows of Pascal's triangle.
#### Soln: 
def pascal_triangle(n):
  trow = [1]
  y = [0]
  for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
  return n>=1
pascal_triangle(6)     

### Q14) Write a Python program to access a function inside a function.
#### Soln: 
def test(a):
        def add(b): ## Parent = fi
                nonlocal a
                a += 1 ## 4+1 = a =5
                return a+b ## = 5+4 --> a+b
        return add
func= test(4) ## a = 4
print(func(4)) ## b = 4


### Q15) Write a Python program to detect the number of local variables declared in a function.
#### Soln: 
def abc():
    x = 1
    y = 2
    str1= "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)