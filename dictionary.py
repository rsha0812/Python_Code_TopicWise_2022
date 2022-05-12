# #### Dictionary: 
# ######dict = {key:value}

##################### Udemy ######################
### Dictionary: 
## Getting Value using method: 
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
value = crypto.get(4)
print(value)

## Getting Value using Key: 
value = crypto[4]
print(value)

## Update: 
crypto[4] = "Cardano"
print(crypto[4])

crypto.update({6:"Monero"})
print(crypto[6])

## Deletin Key (W/O using pop): 
dic1 = {1:10,2:20,3:30,4:40}
del dic1[2]
print(dic1)
## To delete all Items: 
dic1.clear()

## To verify key not in dictionary: 
crypto = {1: "Bitcoin", 2: "Ethereum", 3: "Litecoin", 4: "Stellar", 5: "XRP"}
check = 7 not in crypto.keys()
print(check)
print(sum(crypto))
####################---------------------------------------------------##############################
# ############################# Sorting Dictionary by Key and Value #######################
# d = {'def':300,'abc':200,'ghi':134}
# print(sorted(d)) ### sorted by key 
# print(sorted(d,key=lambda k:d[k])) ### Sorted by Value 
print(sorted(d.values())) # sort the values 


# ########################### Add - Update Dictionary ###############################
# ### Add Key to Dictionary: Using Update 
# d = {0: 10, 1: 20}
# d.update({2:30})
# print(d)

# ### Concatenate Multiple Dict into one using Update: 
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for i in (dic1,dic2,dic3): 
#     dic4.update(i)
#     print(i)
# print(dic4)

# ## Q1)  Write a Python script to check whether a given key already exists in a dictionary.
# ### Soln: 
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}       
# def key_check(k): 
#     if k in d: 
#         print("Available")
#     else: 
#         print("Not available in dict")
# key_check(4) ## Available
# key_check(2) ## Available
# key_check(8) ## Not available in dict

# ## Q2) Write a Python program to iterate over dictionaries using for loops.
# ### Soln: 
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for k in d: 
#     print(k) ## Only key
# for k in d: 
#     print(d[k]) ## Only value
    
# ### to get both key,value --> use items: 
# for k,v in d.items(): 
#     print("Key: {0}, Value: {1}".format(k,v))


# ## Q3)Write a Python script to generate and print a dictionary 
# ##that contains a number (between 1 and n) in the form (x, x*x)
# ### Soln: 
# n = int(input("Enter the number: "))
# d = dict()
# for k in range(1,n+1): 
#     d[k] = k*k
# print(d) ## O/P : {1:1,2:4,3:9,4:16,5:25}

# #Soln 2: 
# def num_sq(n): 
#     new = {}
#     for i in range(1,n+1): 
#         new[i] = i*i
#     return new 
# print(num_sq(5))## O/P : {1:1,2:4,3:9,4:16,5:25}

# ## Soln3: Using Dictionary Comprehension 
# dic = {x: x*x for x in range(1,6)}
# print(dic)
# ######## Merging Dictionaries##############
# ## Q4) Write a Python script to merge two Python dictionaries
# ### Soln: 
# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic_merge = {}
# for i in (dic1,dic2):
#     dic_merge.update(i)
# print(dic_merge)

# #### Soln 2: Merging Dict 
# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic12 = {**dic1,**dic2} 
# print(dic12)


# ######################## Sum of all Values & Keys in a Dictionary #####################################
# ## Q5) Write a Python program to sum all the items in a dictionary. 
# ### Soln: 
# dic1 = {1:10,2:20,3:30,4:40}
# print(sum(dic1.values())) ## O/P : 100 -- Adding all Values 
# print(sum(dic1.keys())) ## O/P : 10 -- Adding all keys 

# ##################### Multiplication ######################## 
# ###### Note : Can have one value as str and rest int or all int 
# ## Q6) Write a Python program to multiply all the items in a dictionary.
# dic1 = {1:1,2:2,3:1,4:'cat'}  #### One Value as Str 
# mul = 1
# for k in dic1: 
#     mul = mul * k 
# print(mul) ### Multiplying Keys -- 24

# for k in dic1: 
#     mul = mul * dic1[k] 
# print(mul) ### Multiplying Values

# ## Or:  All Values as int 
# dic1 = {1:10,2:20,3:30,4:40} 
# mul = 1
# for k in dic1: 
#     mul = mul * k 
# print(mul) ### Multiplying Keys -- 24

# for k in dic1: 
#     mul = mul * dic1[k] 
# print(mul) ### Multiplying Values --- 5760000


# ############### Removing Key/Value #######################
# ## Q7) Write a Python program to remove a key from a dictionary.
# #### Soln: 
# ### Pop: To remove specific key from dictionary 
# dic1 = {1:10,2:20,3:30,4:40}
# dic1.pop(2)
# print(dic1)

### Del :
# dic1 = {1:10,2:20,3:30,4:40}
# del dic1[2]
# print(dic1)

# #### Removing the Last Element in Dictionary: 
# ### PopItem : To remove last element from Dictionary.
# dic1 = {1:10,2:20,3:30,4:40}
# dic1.popitem()
# print(dic1)

# ############ Mapping - Converting List into Dictionary ###################################
# ## Q8) Write a Python program to map two lists into a dictionary.
# ### Soln: 
# ## Using zip: 
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# main_dict = dict(zip(keys,values))
# print(main_dict)

######### Max-Min in Dictionary #############################
## Q9)Write a Python program to get the maximum and minimum value in a dictionary. 
#### Soln: 
my_dict = {'x':500, 'y':5874, 'z': 560}
### Key - Max & Min
print(max(my_dict))
print(min(my_dict))
### Values - Max & Min
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])

######### Removing Duplicate #################################
## Q10) Write a Python program to remove duplicates from Dictionary.
### Soln: 
student_data = {'id1':'sara','id2':'mat','id3':'sara','id4':'pooja','id5':'sana','id6':'sana'}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

######### Empty Dict - Check #########################################
## Q11) Write a Python program to check a dictionary is empty or not.
### Soln: 
my_dict = {}

if not bool(my_dict):
    print("Dictionary is empty")


######### Adding Two Dictionary with Common Key #############################
## Q11)  Write a Python program to combine two dictionary adding values for common keys.
### Soln: ## Basic using loops 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = dict(d1) # don't do `d3=d1`, you need to make a copy
print(d3) ### {'a':100,'b':200,'c':300}
d3.update(d2) 
print(d3) ### {'a':300,'b':200,'c':300,'d':400}
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print(d3) ### {'a':400,'b':400,'c':300,'d':400}

### Soln2: Using Counter 
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 30  , 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

## Q12) Write a Python program to print all unique values in a dictionary
### Soln:
d1 =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] ## Dicts in List = [{},{}]
## Query Breakdown: 
# for i in d1: ## for list 
#     for v in i.values(): ## for values in dictionary inside the list 
#         print(v)
uniq_val = set(v for i in d1 for v in i.values()) ## set(list) --> to get unique value set comprehension
print("The Unique Values are: ",uniq_val)

############ Dictionary in Table Format ##################################### 
## Q13) Write a Python program to print a dictionary in table format.
### Soln: 
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)

## Q14) Write a Python program to access dictionary key's element by index.
### Soln: 
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])

############# Depth of Dictionary ###############
## Q15) Write a Python program to get the depth of a dictionary.
### Soln: 
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))

### Note : isinstance(object, type) : The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#### to use map() function by which the values of the inner dictionary is mapped to the called function.
### for more soln : https://www.geeksforgeeks.org/python-find-depth-of-a-dictionary/
    
################ Group By ######################
from itertools import groupby
things = [("animal","bear"),("animal","cat"),("plant","cactus"),
            ("vehicle","car"),("vehicle","bus")]
dic = {}
f = lambda x : x[0]
for key, group in groupby(sorted(things,key = f), f): 
    dic[key] = list(group)
print(dic)

############ Dictionary Comprehension ####################3
## Qn : Write a dict comprehension in range(9) and return key-value pair where value is 3 times of key. 
### Soln: 
cph = {x: x * 3 for x in range(9)}
print(cph)

########### Dictionary - Geeks for Geeks #########################
