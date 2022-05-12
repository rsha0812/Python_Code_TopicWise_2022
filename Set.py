# Practise - Source - https://www.w3resource.com/python-exercises/sets/
####Practise Question for Strings: 

### Definitions Of Set : A set is an unordered collection with no duplicate elements. Curly braces or the set() function can be used to create sets.

#### Removing Dupliactes : 
lst = [1,2,3,3]
print(set(lst))

### To create Frozet Set : 
a = {1,2,3,'foo','bar'}
frozen = frozenset(a)
print(frozen,type(frozen))
## Q1) Write a Python program to create a set.
### Soln: 
lst = [1,2,3,3]
set_lst = set(lst)
print(lst,type(lst)) ## O/P = [1,2,3,3],List
print(set_lst,type(set_lst))  ## O/P = {1,2,3},set

### Creating Set Using {} Bracket:
a = {1,2,3,'foo','bar'}
ax = [1,2,3,'foo','bar']
print(a,type(a)) ## type = set --> {}
print(ax,type(ax)) ## type = list --> []


## Q2) Write a Python program to iteration over sets.
## Soln: 
a = {1,2,3,'foo','bar'}
for i in a: 
    print(i, end = ' ') ### end = '' --> to get output in one line 


#### Adding Single/Multiple Element in Set ##################
## Q3) Write a Python program to add member(s) in a set.
## Soln: 
a = {1,2,'dog'}
print(a)

## Add: 
a.add('cat') ## To Add a single element in set  - add
print(a,type(a))

## Update: 
a.update(['mat','rat',4,5]) ## To Multiple Element in set - update
print(a,type(a))

### Update: 
a = {1,2,3}
b = {4,5,6}
a.update(b)
print(a) ## O/P : {1,2,3,4,5,6}
print(b) ## O/P: {4,5,6}

###################### Removing Element from Set ##############################3
## Q4) 
### Soln: 
a = {1,2,'dog','cat','rat',4,'mat',5}
### Remove:
a.remove('mat')  ### Removed Specified Element from Set  --- Remove(takes 1 arg)
print(a)  ## Remove mat

### Pop:
a.pop() ### Removed first element from Set --- Pop
print(a) ## remove 1{1st element of set}

### Discard: 
a.discard(4)  ### Remove specified Element --- Discard(takes one arg)
print(a) ### Remove 4 from set 

### Clear: 
a.clear() #### To remove all Elements from set 
print(a)   ## O/P: set() -- empty set 

######################## Join Methods ############################################################

a = {1,2,3,4,5,6,7,9}
print("Set A")
print(a,type(a))
b = {4,5,8,9,11,7,18,10}
print("Set B")
print(b,type(b))

### intersection of two sets(Gives common element of both sets)
print("Intersection of Set A and Set B")
intersect = a & b
print(intersect) ## O/P : {9,4,5,7}

### Union: The union() method returns a new set with all items from both sets:
print("Union of Set A and Set B")
union_set = a.union(b)
print(union_set)  ### Without Duplicate

### difference: to create set difference -- Gives unique value of set which is not available in other set.
diff_set_a = a.difference(b)
diff_set_b = b.difference(a)
print(diff_set_a) ## O/P: {1,2,3,6} --> Gives unique value of Set A
print(diff_set_b) ## O/P: {8,18,10,11} --> Gives unique value of Set B
### Analysis: Removes common element of both set and gives O/P as unique element of that particular set.

### Symmetric difference: the symmetric difference of the sets {1,2,3} and {3,4} is {1,2,4}.
sym_diff_a = a.symmetric_difference(b)
print(sym_diff_a) ## O/P: {1,2,3,6,8,10,11,18}
sym_diff_b = b.symmetric_difference(a)
print(sym_diff_b) ## O/P: {1,2,3,6,8,10,11,18}
### Analysis: Removes common element of both set and gives O/P as combination of unique element of both sets.

#### SubSet & SuperSet -- Sets #################
## Defn : set A is a subset of set B if all elements of A are also elements of B; B is then a superset of A.
## Syntax : issubset() 
a = {1,2,3}
b = {1,2,3,4,5,6} 
print(a.issubset(b)) ### True: as all element of is in b 
c = {8,4,5,6}
print(c.issubset(b)) ### False: as c{8} is not in b 

########################### Shallow Copy##########################################
### Defn : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
#### Soln: 
setp = set(["Red", "Green"])
setq = set(["mat","cat"])
#A shallow copy
set_copy_p = setp.copy()
set_copy_q = setq.copy()
print(set_copy_p,type(set_copy_p))
print(set_copy_q,type(set_copy_q))

########################## Max-Min #####################################
seta = {1,2,3,4,5,6} 
setb = {4,5,8,9,11,7,18,10}
setc = {'cat','mat','rat'}
print(max(seta))
print(min(seta))
print(max(setb))
print(min(setb))
print(max(setc)) ## --> Follow alphabetical order for max & min
print(min(setc))

######################### Length Of Set ################################
seta = {1,2,3,4,5,6} 
setb = {4,5,8,9,11,7,18,10}
setc = {'cat','mat','rat'}
print(len(seta)) ## 6
print(len(setb)) ## 8
print(len(setc)) ## 3

###################################################################################################
## Q5) Write a Python program to find the elements in a given set that are not in another set.
### Soln:
## Using difference()
seta = {1,2,3,4,5,6} 
setb = {4,5,8,9,11,7,18,10}
print(seta.difference(setb))
### Or - Anaother Way using (-)
print(seta - setb)

########### Checking Common Element in Sets(Using isdisjoint) #############################
## Q6) Write a Python program to check if two given sets have no elements in common.
#### Soln: 
####### Using isdisjoint: 
x = {1,2,3,4}
y = {4,5,6,7}
z = {8}

print("Comparing Set x and y: ")
print(x.isdisjoint(y)) ## False : as x n y has common elements
print("Comparing Set x and z: ")
print(x.isdisjoint(z)) ## True : as x n z has no common elements
print("Comparing Set z and y: ")
print(z.isdisjoint(y)) ## True : as y n z has no common elements

######### Set Comprehension ############################################
### Qn : Write a set comprehension that will iterate over range(10,19) and return set of elements divided by 2.5.
### Soln: 
cph = {x / 2.5 for x in range(10, 19)}
print(cph)