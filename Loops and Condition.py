####Condition: ---- Udemy 250 Questions: 
## Qn: Print Out "True!" if any of the condition occurs: 
## 1) String contains character z 
## 2) string contain character y atleast twice.
## Soln: 
x = "The days of Python 2 are almost over. Python 3 is the king now."
if "z" in x or x.count("y") >= 2: 
    print("True!")

## Qn: Print "True!" if the index of first occurence of 'f' is less than 10 else print "False!"
x = "The days of Python 2 are almost over. Python 3 is the king now."
if x.index('f') < 10: 
    print("True!")
else: 
    print("False!")
    
## Qn: Check last three characters of the string are digit.
## Soln: 
x = "The days of Python 2 are almost over. Python 3 is the king now."
if x[-3:].isdigit():
    print("True!")
else: 
    print("False!")
    
## Qn: Print True if list has atleast 8 elements and the element at index 6 is float: 
## Soln: 
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]
if len(x) >= 8 and type(x[6]) is float: 
    print("True!")
else:
    print("False!")

## Qn: Print "True!" if the second string of the first list in x ends with ("h) ##and the first string in second list end with ("h").
## Soln: 
x = [115, 115.9, 116.01, ["length", "width", "height"], 109, 115, 119.5, ["length", "width", "height"]]

if x[3][1].endswith("h") and x[7][0].endswith("h"): 
    print("True!")
else:
    print("False!")
    
## Qn: Compare the largest value among first 3 elements of list less than or ##equal to next 3 elements of list: 
## Soln: 
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
if max(x[:3]) <= min(x[3:6]): 
    print("True!")
else: 
    print("False!")
    
## Qn: To check 115 is in list "x" or first element of list. 
## Soln: 
x = [115, 115.9, 116.01, 109, 115, 119.5, ["length", "width", "height"]]
if 115 in x or x[0] == 115: 
    print("True!")
else: 
    print("False!")
    
## Soln 2: 
if x.count(115) >= 1 or x.index(115) == 0:
    print("True!")
else:
    print("False!")
    
# Qn : If the value of key 5 is "Perl" or number of key-value pair in dict when divided by 5 return remainder less than 2: 
# Soln1: 
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if x[5] == "Perl" or len(x)%5 < 2: 
    print("True!")
else:
    print("False!")

## Qn: Print True if 3 in dict and smallest values(alphabetically) is 'C#'.
## Soln: 
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if 3 in x.keys() and sorted(x.values())[0] == 'C#': 
    print("True!")
else:
    print("False!")
    
## Qn: To check last sorted value's last character is n.
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if sorted(x.values())[-1][-1] == 'n': 
    print("True!")
else:
    print("False!")
  
  
## Qn : if largest key divided by second largest key is equals to smallest key then return "True!"  
## Soln1: 
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if (sorted(x)[-1]//sorted(x)[-2]) == min(x): 
    print("True!")
else: 
    print("False!")

# Soln2: 
if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("True!")
else:
    print("False!")

## Qn: Print True if sum of all the keys in the dictionary is less than number of ##character of the strings concatenating the values of first 5 keys.
## Soln: 
# x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if sum(x) < len(x[1]+x[2]+x[3]+x[4]+x[5]): 
#     print("True!")
# else: 
#     print("False!")
    
##Qn: Print True if 3rd element of first range is less than 2, print False if 5th element of first range is 5, else print None.
## Soln: 
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
if x[0][2] < 2: 
    print("True!")
elif x[0][4] == 5: 
    print("False!")
else: 
    print("None!")

### Qn: Comparing sum of the ranges. 
## Soln: 
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
 
if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")

## Qn: Print True, if 2nd character of the value at key1 is also present in value of 4th key.
## Soln: 
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
# if x[1][1] in x[4]: 
#     print("True!")
# else: 
#     print("False!")

## Qn: if number of character of smallest value in dictionary is equal to no. of occurence of letter a in the value at key 3.
## Soln: 
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
if (len(min(x.values()))) == (x[3].count("a")): 
    print("True!")
else: 
    print("False!")

######## Loops ###################
### Loop - Udemy : 
### For Loop: 
## Qn: Print all the element of list in reverse order and multiplied by 10.
## Soln1:
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x[::-1]:
    print(i*10)
    
# Soln2: 
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x: 
    if i%2 == 0: 
        print(i)
print("Great job!")


## Qn: Print all the element in list divided by 2 and print the string "Great job!" after the list is exhausted.
## Soln: 
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x:
    print(i / 2)
else:
    print("Great job!")
    
# Qn: Print Out the index of each element in list: 
# Soln: 
x = [10, 12, 13, 14, 17, 19, 21, 22, 25]
for i in x: 
    print(x.index(i))
    
##### While Loop: 
# Qn: Print out value of 10 times x till x is less than or equal to 4. Print "Done!" once x > 4.
# Soln:
x = 0
while x <= 4: 
    print(10*x)
    x+=1
else: 
    print("Done!")
    
## Qn: Print out y times x when x is greater or equal to 5, and print out x divided by y when x = 10.
## Soln:
x = 5
y = 2
while x >= 5 and x < 10:
    print(x * y)
    x = x + 1
else:
    print(x / y)

## Qn: Multiply element with last element of range if the element is between [3,8] inclusive. else: Print("Outside!")
## Soln: 
for i in range(1,11,2): 
    if 3 <= i <=8: 
        print(i * range(1,11,2)[-1])
    else: 
        print("Outside!")

## Qn: Print out the value of x times 11 when x is less than or equal to 11 and when x == 10, then print "x is 10!".
## Soln: 
x = 5
while x <= 11: 
    if x == 10: 
        print("x is 10!")
        x = x+1
    else: 
        print(11*x)
        x = x+1

### Break : 
## Code1:
x = [1, 2]
y = [10, 100]
 
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
        print(i)
        break
    print(j)

## Code2:
x = [1, 2]
y = [10, 100]
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            break
        print(i)
    print(j)

## Code 3: 
x = [1, 2]
y = [10, 100]

for i in x:
    for j in y:
        if i % 2 == 0:
            break
            print(i * j)
        print(i)
    print(j)

### Continue:
## Code1: 
x = [1, 2]
y = [10, 100]
for i in x:
    for j in y:
        if i % 2 == 0:
            print(i * j)
            continue
        print(i)
    print(j)

## Code2: 
x = [1, 2]
y = [10, 100]
for i in x:
    for j in y:
        if i % 2 == 0:
            continue
            print(i * j)
        print(i)
        
    print(j)

#### Conditions & Loop Statement : https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

### Q1) Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
### between 1500 and 2700 (both included).
### Soln:
nl = []
for i in range(1500,2701): 
    if (i%7==0) and (i%5==0):
        nl.append(str(i))
print(",".join(nl)) ## Join the string in O/P. 

### Q2) Write a Python program to guess a number between 1 to 9.
### Soln:
# import random
# target_num, guess_num = random.randint(1, 10), 0 ## initially guess_num = 0 & target_num --> Any random num
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')
# ### print(random.randint(1, 10)) --> Will give random number 


############# Patterns #####################
### 1) 
for i in range(6): 
    print()
    for j in range(6): 
        if i == j:
            print('*',end ='')
        else: 
            print('#',end='')
### 2) 
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print ('* ', end="")
    print('')

### 3) 
for i in range(5): 
    print() 
    for j in range(6): 
        if (i>=j): 
            print("*",end=" ")
        else: 
            print("#",end=" ")

### 4) Printing Alphabet 'A': 
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);


############ Reversing the Word ##################
### Q4) Write a Python program that accepts a word from the user and reverse it.
### Soln:
## Sol1: using Reverse
word = input("Enter the Word: ")
rev_word = (list(reversed(word)))
print("".join(rev_word))
    
## Sol2: Using For loop: 
word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")

## Sol3: Using While loop: 
word = input("Input a word to reverse: ")
rev_word = ""
i = len(word)-1
while(i)>=0: 
    rev_word = rev_word + word[i]
    i = i-1
print(rev_word)

######## Count #############################
### Q5) Write a Python program to count the number of even and odd numbers from a series of numbers.
### Soln:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even_cnt = 0
odd_cnt = 0 
for i in numbers: 
    if (i%2==0):
        even_cnt += 1
    else: 
        odd_cnt += 1
print("The Count of Even Number is : ",even_cnt)
print("The Count of Odd Number is : ",odd_cnt)


###### Continue ################
### Q6) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
### Soln:
num = (1,2,3,4,5,6,7,8,9,0)
for i in num: 
    if i==3 or i==6: 
        continue
    print(i,end=' ') ## To get output in One Line

##### Fibonnaci Series###############
### Q7) Write a Python program to get the Fibonacci series between 0 to 50
### Soln:
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y

### Q8) Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
### Soln:
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for i in lines:
    print(i)

############ To Chech the type(isdigit/isalpha)######################
### Q8) Write a Python program that accepts a string and calculate the number of digits and letters.
### Soln:
strng = 'Python 3.2'
l = d = 0
for i in strng: 
    if i.isalpha(): ## To check letters or chars
        l+=1 
    elif i.isdigit(): ## to check int/number
        d+=1
    else: 
        pass 
print("Total Letter in Strng: ",l)
print("Total Digits in Strng: ",d)

###### Time - Year,Age,Month Calculation ####################
### Q8) Write a Python program to calculate a dog's age in dog's years.
###Note: For the first two years, a dog year is equal to 10.5 human years. 
##After that, each dog year equals 4 human years.
##Input a dog's age in human years: 15                                    
##The dog's age in dog's years is 73
### Soln:
h_age = int(input("Enter the Dog Age in Human Year: "))
if h_age < 0: 
    print("Age must be positive integer")
    exit()
elif h_age <=2: 
    d_age = h_age * 10.5
else: 
    d_age = 21 + (h_age - 2) * 4  ## Subtracted 2 as two years = 21 
print("Dog's Age in Dog's Year: ",d_age)


### Q8) Write a Python program to check whether an alphabet is a vowel or consonant.
#### Soln: 
alpha = input("Enter the Alphabet: ")
vow = 'aeiou'
if alpha.lower() in vow: 
    print("{0} is a Vowel".format(alpha))
else: 
    print("{0} is a Consonant".format(alpha))


################### Median ################################ 
### Q9) Write a Python program to find the median of three values.
#### Soln: 
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)
