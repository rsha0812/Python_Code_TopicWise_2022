### List 
#### List - Udemy 

## To Check Number of Elements: 
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
char = len(my_list)
print(char)

## To Remove Element at index 5. : Pop - Remove element by Index
my_list.pop(5)
print(my_list) ## Java removed 

## To add Element in List: 
my_list.append("C++")
print(my_list)

## Remove: Remove element by Values 
my_list.remove(30)
print(my_list)

## To Get Index of a Value: 
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']
index = my_list.index(10.5)
print(index)

### To Insert Element at given Inder 
my_list.insert(4,77) ## Inserting 77 at index 4 
print(my_list)

## Extending the List: 
my_list.extend([100,101,102])
print(my_list)

## Count Occurence of the Element: 
howmany = my_list.count(20)
print(howmany)

### Sorting 
# '''
# Defination:
# list.sort(): sorts the list elements in ascending order; modifies the list in place
# ist2.reverse(): sorts the list elements in descending order; modifies the list in place
# sorted(list2): sorts the elements of a list in ascending order and creates a new list at the same 
# time
# sorted(list2, reverse = True): sorts the elements of a list in descending order and creates a new list at the same time
# '''
## Sorting List in Ascending Order: 
my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
asc = sorted(my_list)
print(asc)

## Sorting List in Descending Order: 
asc = sorted(my_list, reverse = True)
print(asc)

### To Sum all Elements of List: 
add = sum(my_list)
print(add)

##### Itertools###########
### Qn : Concatenate list1 and list2 using itertools. 
### Soln: 
### Method1 : Using itertools.chain 
import itertools
list1 = [1, 2, 3]
list2 = [4, 5]
result = list(itertools.chain(list1, list2))
print(result)

### Method2: Using extend
list1 = [1, 2, 3]
list2 = [4, 5]
(list1.extend(list2))
print(list1)

### Qn : Use correct function from itertools that return all the numbers from 20 to 31 with step of 2.
#### Soln: 
import itertools
for i in itertools.count(20,2): 
    if i < 31: 
        print(i)
    else: 
        break

### Qn: Use itertools function to return the elements for which lambda function gives arguement as False.
### Soln: 
import itertools
lam = lambda x: x < 5
result = list( itertools.filterfalse(lam, range(10)))
print(result) ### O/P : [5, 6, 7, 8, 9]

# ########## Sorting List of Tuple #########################
# ## Q1) Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#### Formula Used : sorted(lst_name,key=function_applied)
lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
f = lambda x:x[1]
print(sorted(lst,key =f))
#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]  --> Output

### Reverse 
lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
f = lambda x : x[1]
print(sorted(lst,key = f,reverse = True)) ## O/P: [(2, 5), (4, 4), (2, 3), (1, 2), (2, 1)]

########### Sorting Nested Dictionaries ############
### Q) Write a Python program to sort a list of nested dictionaries.
#### Sol: 
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True) ### In reverse --> e(value of key)(value of subkey)
print("Sorted List: ")
print(my_list)
lst = [{'x':{'a':1}},{'x':{'a':2}}]
lst.sort(key=lambda e: e['x']['a'],reverse = True)
print(lst)

######### Remove Duplicate ###################
## Q2) Write a Python program to remove duplicates from a list.
### Soln: 
a = [10,20,30,20,10,50,60,40,80,50,40]
res = []
for i in a: 
	if i not in res: 
		res.append(i)
print(res) ## O/P : Ordered List 
### Sol2: Using Set
res = set(a)
print(res) ## O/P : Unodered set

######## Check - Empty List ##################################
##Q) Write a Python program to check a list is empty or not.
### Soln: 
l = [1,2]
if not bool(l): ##(or --> if not l:)
	print("Empty")
else: 
	print("Not Empty")

######## Copy/Clone List ###################
## Q) Write a Python program to clone or copy a list.
#### Soln: 
original_list = [10, 22, 44, 23, 4]
new_lst = list(original_list)
print("The new list is {}".format(new_lst))

### Sol2: Slicing: 
original_list = [10, 22, 44, 23, 4]
copy_lst = original_list[:]
print(copy_lst)

##Q) Write a Python function that takes two lists and returns True if they have at least one common member.
#### Soln1: 
a = [1,2,3,4,5]
b = [5,6,7,8,9,4]
for i in a: 
	for j in b: 
		if i == j : 
			print(i)
## Sol2:
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

############# Flattening List ###################
##Q) Write a Python program to flatten a shallow list. 
## Soln:
# Sol1-Using Nested List 
lst = [[2,4,3],[1,5,6], [9], [7,9,0]]
flat_lst = []
for i in lst: 
	for j in i: 
		flat_lst.append(j)
print(flat_lst)
		
## Sol2-Using  List Comprehension
flat_lst = [j for i in lst for j in i]
print(flat_lst)

## Sol3 - Itertools
import itertools
flat_lst = itertools.chain(*lst)
print(list(flat_lst))

########### Converting List into String ###################### 
#Q) Write a Python program to convert a list of characters into a string. 
#### Sol: 
lst = ['e','n','d']
str_lst = "".join(lst)
print(str_lst)

##Q) Write a Python program to create a list of empty dictionaries.
### Soln: 
l = [{} for i in range(3)]
print(l)

######### Remove Duplicates from list of list ##########
##Q) Write a Python program to remove duplicates from a list of lists.
### Sol1: Using itertools + groupby() 
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
num.sort()
print(num)
new_num = list(num for num,i in itertools.groupby(num))
print(new_num)
### Breaking Code Logic :
# for x,i in itertools.groupby(num): 
# 	print(x,i) ---- [10,20]...[30, 56, 25]...[33]...[40]

#### Converting Lists into Dictionary ##########
l1 = [10, 20] 
l2 = [30, 56, 25]
dic = dict(zip(l1,l2))
print(dic)

#### Zipping two Lists ########## 
###Q) Write a Python program to Zip two given lists of lists.
### Soln: 
list1 = [[1, 3], [5, 7], [9, 11]] 
list2 = [[2, 4], [6, 8], [10, 12, 14]]   
print("Original lists:")
print(list1)
print(list2)
result = list(map(list.__add__, list1, list2))
##print(result) 
print("\nZipped list:\n" +  str(result))

##### Different Ways to Clear List in Python #################
### code: 
## 1) Using Clear:
test_list = [ 1, 6, 3, 5, 3, 4 ]
test_list.clear()
print(test_list)

## 2) Using del: 
test_list2 = [ 1, 6, 3, 5, 3, 4 ]
print(test_list2)
del (test_list2[:])
print("List after deleting : ",test_list2)

#### Reversing the List ##################
### 1) Using Reverse:
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print(lst)

### 2) Using Negative Index:
lst = [10, 11, 12, 13, 14, 15]
print("Reversed List: ",lst1[::-1])

### 3) Reversing a list using reversed()
def Reverse(lst):
    return [ele for ele in reversed(lst)]
# Driver Code
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

###### REmoving Empty Tuples from the list ###########     
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                 ('krishna', 'akbar', '45'), ('',''),()]
new_tup = []
[new_tup.append(i) for i in tuples if i != ()]
print(new_tup)

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                 ('krishna', 'akbar', '45'), ('',''),()]
new_tup = filter(None,tuples)
print(list(new_tup))

##### Converting List to List of `Dictionaries ###### (IMP)
value_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ["name", "number"]
n = len(value_list)
res = [] 
for i in range(0,n,2): 
    res.append({key_list[0]:value_list[i],key_list[1]:value_list[i+1]})
'''
res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx + 1]}
       for idx in range(0, n, 2)]--> Using List Comprehension instead of Loop'''
print(res)

##### Convert Lists of List to Dictionary ######
'''
The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]]
The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}'''
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
res = {tuple(sub[:2]):tuple(sub[2:]) for sub in test_list}
print(res)

########## Uncommon elements in Lists of List ######## 
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
### Soln 1:
res = []
for i in test_list1: 
    if i not in test_list2: 
        res.append(i)
for j in test_list2: 
    if j not in test_list1: 
        res.append(j)
print(res)
### Soln2: 
res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
## use of ^ operator can perform the set symmetric difference - gives unique ##element from both sets.
res_list = list(map(list, res_set))
print(res_list)

##### To select Random from List of Lists ######
'''
Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix.'''
import random
from itertools import chain
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
### Chain will flatten the list 
### choice for random numbers 
res = random.choice(list(chain.from_iterable(test_list)))
print(res)

##### Reverse Row sort in Lists of List ##### 
'''
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]'''
org_lst = [[4, 1, 6], [7, 8], [4, 10, 8]]
new_lst = []
### Soln1: Using Sorted()
for i in org_lst: 
    i = sorted(i,reverse = True)
    new_lst.append(i)
print("Sorting List using Sorted():",new_lst)

### Soln2 : Using Sort() 
for i in org_lst: 
    i.sort(reverse = True)
print("Sorting List using sort():",org_lst)

### Sol3: LC + Sorted() 
new = [sorted(i,reverse = True) for i in org_lst]
print("Sorting List using LC and Sorted:",new)


###### Pair elements with Rear element in Matrix Row ######
'''
The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]'''
 ### Soln: 
 
org_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
res = []
for i in org_list: 
    res.append([[ele,i[-1]] for ele in i[:-1]])
print(res)

### Code Break Analysis : 
for i in org_list: 
    for x in i[:-1]: 
        print(x) ## 1st and 2nd element of sublist 
        print([x,i[-1]]) ## combine element with last element of sublist 

#######----------------------------------------------------------------------------------------##############################
#### Advanced List Program ############## 
###### How to count unique values inside a list #########
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
### Brute Force Approach - Not recommended 
count = 0 
new = []
for i in input_list: 
    if i not in new: 
        count += 1
        new.append(i)
        
print("Unique element in the List:",count)

### Using Counter
from collections import Counter
items = Counter(input_list).keys()
print("Items:",items)
print("No of unique items in the list are:", len(items))


###### Test if List contains elements in Range ##################
test_list = [4, 5, 6, 7, 3, 9]
test_list1 = [4, 5, 6, 7, 3, 9,11]
## Initializing range : 
i,j = 3,10 
res = all(ele >= i and ele < j for ele in test_list) 
res1 = all(ele >= i and ele < j for ele in test_list1) 
print(res) ## True as all elements are in range of 3 and 10
print(res1) ## False as all elements are not in range of 3 and 10

####### Python program to find the Strongest Neighbour #########
'''
Input: 1 2 2 3 4 5
Output: 2 2 3 4 5'''
### Code: 
arr = [1,2,2,3,4,5]
new = []
for i in range(1,len(arr)): 
    res = max(arr[i],arr[i-1])
    new.append(res)
print(new)

####### to print the element which occurs 3 consecutive times in a Python list#########
'''
Input : [4, 5, 5, 5, 3, 8,8,8]
Output : 5 8'''
lst = [4, 5, 5, 5, 3, 8,8,8]
for i in range(len(lst)-2): 
    if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:
            print(lst[i])


####### Remove all the occurrences of an element from a list in Python ###
## Input : 5 6 7 8 9 10 7 Output : 5 6 8 9 10
### Using remove
lst = [5,6,7,8,9,10,7]
k = 7 
for i in lst: 
    if i == k : 
        lst.remove(k)
print(lst) ### O/P: [5,6,8,9,10]
#### Using LC
new = [] 
[new.append(i) for i in lst if i!=k]
print(new) ### O/P: [5,6,8,9,10]

####### Program to print all Possible Combinations from the three Digits ###
'''
Input: [1, 2, 3]
Output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1'''
### Method1: Loop- Brute force: 
lst = [1, 2, 3]
for i in range(3): 
    for j in range(3): 
        for k in range(3): 
            if i!=j and j!=k and k!=i: 
                print(lst[i],lst[j],lst[k])
### Method2: Using Itertools Permutation 
from itertools import permutations
comb = permutations([1, 2, 3], 3)
for i in comb:
    print(i)


##### Extract elements with Frequency greater than K ########
### Method1 : Using count() + loop 
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
new = []
for i in test_list: 
    freq = test_list.count(i)
    if freq>k and i not in new: 
        new.append(i)
print(new)

### Method2 : Using list comprehension + Counter()
from collections import Counter
test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
K = 2
# using list comprehension to bind result
res = [ele for ele, cnt in Counter(test_list).items() if cnt > K]
print(res)

