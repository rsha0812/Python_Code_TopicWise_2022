# Practise - Source - https://www.w3resource.com/python-exercises/string/
####Practise Question for Strings: 

#####----------------------###################################################################
###### Udemy Questions: 
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
 
print(my_string[-9]) ## o --> to get string 
print(my_string.index("B")) ## 26 ---> To get index of string 
print(my_string.count("o")) ## 5 --> To get occurence of "o"
print(my_string.upper()) ### To convert in UpperCase 
print(my_string.find("Bitcoin")) ### To get index of the string 
print(my_string.startswith("X")) ###  checking whether the string starts with a ##character
print(my_string.swapcase()) ## To convert Upper into Lower and lower into upper
print(my_string.strip())
print(my_string.replace(" ", "")) ### To remove white space in the sentence
print(my_string.replace("i","btc")) ## Replacing occurence of i with btc
print(my_string.split(",")) ## Spliting the character from comma(,)
print("&".join(my_string)) ## Join all using &
#### Concatenating : 
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
my_other_string = "Poor guy!"
print(my_string + my_other_string)

## To convert the first letter of each word into UpperCase: 
print(my_string.title()) 

#### String Formatting: 
## "%s"
my_string = "In %s, someone paid %s %s for two pizzas."
print(my_string %("2010","10k","Bitcoin"))

##{} 
my_string = "In {}, someone paid {} {} for two pizzas."
print(my_string.format("2010","10k","Bitcoin"))

#### Slicing
my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(my_string[3:7])
print(my_string[-23:-16])
##############---------------------------------------------#####################################

##Q1) to count the number of characters (character frequency) in a string: 
###Sol: 
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

##Q2) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
### If the string length is less than 2, return instead of the empty string.
###Soln: 
str1 =  'w3resource'
result = ""
for i in str1: 
    if len(str1)>=2: 
        result = str1[:2] + str1[-2:]
print(result)

str2 =  'w3'
result = ""
for i in str2: 
    if len(str1)>=2: 
        result = str2[:2] + str2[-2:]
print(result)

str3 =  'w'
result = ""
for i in str3: 
    if len(str3)>=2: 
        result = str3[:2] + str3[-2:]
print(result) 

############## Replace = string.replace(oldvalue, newvalue, count) ########
####Q3) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
## except the first char itself.
#####Soln: 
def char_change(s): 
    char = s[0] ## char = r
    s = s.replace(char,'$') ### $esta$t
    s = char + s[1:]   ## r + esta$t
    return s ### resta$t -- Output 
print(char_change('restart'))

### Soln2 : 
s = "return"
char = s[0]
s = s.replace(char,'$') 
print(s)
print(char + s[1:])

################Swapping Characters ########################
##Q4) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
## Soln: 
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]  ## xy+c
  new_b = a[:2] + b[2:]  ## ab+z

  return new_a + ' ' + new_b ### xyc abz -- Output
print(chars_mix_up('abc', 'xyz'))

############### String Change ################
###Q5)Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
##If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. 4
##Soln:
  ## 1) adding 'ly' at the end if string ends with 'ing'
  ## 2) Replacing "ing" with "ly"  if string ends with 'ing'

def add_strng(s): 
    if len(s)>2: 
        if s[-3:] == "ing": 
            s = s.replace("ing","ly") ## Replacing "ing" with "ly" 
            #s += "ly" ## adding 'ly' at the end
        else: 
            s += "ing"
    return s 
print(add_strng('abc'))
print(add_strng('string'))
print(add_strng('st'))

###################### Max Len Word in List####################
###Q6) Write a Python function that takes a list of words and return the longest word and the length of the longest one.
###Soln: 
def longest(lst): 
    word = lst[0]
    for i in lst: 
        if len(word) < len(i): 
            word = i
    return word,len(word)
print(longest(["good","longer","mat","do","done"]))

###########  Removing Index from String #######################
###Q7) Write a Python program to remove the nth index character from a nonempty string.
def remove_indx(str1,n): 
    first_part = str1[:n]
    last_part = str1[n+1:]
    return first_part + last_part
print(remove_indx("Python",3))
print(remove_indx("Python",0))
print(remove_indx("Python",5))

###Q8) Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 
## Soln: 
def str_swap(str1): 
    new_str = str1[-1]+str1[1:-1]+str1[0]
    return new_str
print(str_swap("Python"))
print(str_swap("Lion"))
print(str_swap("Elephant"))

################## Occurence of Word in Sentence#################
##Q9) Write a Python program to count the occurrences of each word in a given sentence.
###Soln: 
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

#################### Upper-Lower ############
###Q10)  Write a Python script that takes input from the user and displays that input back in upper and lower cases.
    
def upper_lower(str1): 
    upper = str1.upper()
    lower = str1.lower() 
    return (upper,lower)
print(upper_lower("Python"))

######################   Removing Duplicates ######################
### Removing Duplicate Using List Comprehension: 
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
[res.append(x) for x in test_list if x not in res]
print(res)

### Removing Duplicate Using Set:
test_lst1 = ['air','cat','bag','dog','cat','dog']
print(list(sorted(set(test_lst1)))) 

# ### Removing Duplicate Using List Comprehension & Enumerate: 
# test_list = [1, 3, 4,5,7, 6, 3, 5, 6, 1]
# for n,i in enumerate(test_list):
#     if i in test_list[:n]: 
#         print(i)
# n = len(test_list)
# print(test_list[:n]) ----- Basic Query 
test_list = [1, 3, 4,5,7, 6, 3, 5, 6, 1]
res_unique = [i for n,i in enumerate(test_list) if i not in test_list[:n]] ### Will give unique value of list
print(res)

test_list = [1, 3, 4,5,7, 6, 3, 5, 6, 1]
res_duplicate = [i for n,i in enumerate(test_list) if i in test_list[:n]] ### Will give duplicate value of list
print(res)

####################### Remove duplicate words from Strings in List ##############
### Method #1 : Using set() + split() + loop
test_list = ['gfg, best, gfg', 'I, am, I', 'two, two, three' ]
res = []
for strs in test_list:
    res.append(set(strs.split(", ")))
    #print(set(strs.split(", ")))
print(res)

### Method #2 : Using list comprehension + set() + split()
test_list = ['gfg, best, gfg', 'I, am, I', 'two, two, three' ]
res = []
[res.append(set(strs.split(", "))) for strs in test_list]
print(res)

### Reversing the String ##########################
###Q11) Write a Python function to reverses a string if it's length is a multiple of 4.
###Soln: 
def rev_str(str1): 
    n = len(str1)
    if n%4 == 0: 
        new_str = str1[::-1]
        return new_str
    else: 
        return str1
print(rev_str("Pythoned"))
print(rev_str("good"))
print(rev_str("be"))


########### UPPER/Lower - isupper()/islower() ####################
###Q12) Write a Python function to convert a given string to all uppercase 
###if it contains at least 2 uppercase characters in the first 4 characters.
###Soln:
def str_upper(str1): 
    if str1[:2].isupper():
        str1 = str1.upper()
    return str1
print(str_upper("PYthon"))
print(str_upper("Lotus"))
print(str_upper("GOOgle"))

############ Join ###########################
str1 = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

def join_str(str1): 
    return " ".join(str1)
print(join_str(['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']))

########## Lower #########################
###Q13) Write a Python program to lowercase first n characters in a string.
#### Soln: 
str1 = "BADMINTON"
new_str = [i.lower() for i in str1[:4]]
print(new_str)
    
######### Count = len in List Comprehension ##############
###Q14) Write a Python program to count and display the vowels of a given text.
####### Soln: 
def vowels(str1): 
    vow = "aeiou"
    final = [i for i in str1 if i in vow]
    return final,len(final)
print(vowels("Badminton"))

####### Removing Leading Zeros ##################
###Q15) Write a Python program to remove leading zeros from an IP address.
####### Soln: 
def remove_zeros_from_ip(ip_add):
  new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
  return new_ip_add ;
print(remove_zeros_from_ip("255.024.01.01"))
print(remove_zeros_from_ip("127.0.0.01 "))

##----- Breaking Above Logic Query 
ip_add = "255.024.01.01" 
print(ip_add.split(".")) ## ['255','024','01','01']
for i in ip_add.split("."): 
    print(str(int(i)))## will remove leading zero and then joinin all by using .join
