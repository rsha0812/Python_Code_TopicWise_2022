# Practise - Source - https://www.w3resource.com/python-exercises/tuple/
####Practise Question for Tuple:

################################Tuple - Udemy ################################################
## To Find out the last element in tuple in alphabetical Order: 
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary")
last = max(my_tup)
print(last) #should return Slovenia

## Counting Occurrence
number = my_tup.count("Estonia")
print(number)

########## Unpacking Tuple ############################
###Q1)  Write a Python program to unpack a tuple in several variables.
####Soln: 
tup = (1,2,3,4)
a,b,c,d = tup
print(a,b,c,d)

tup1 = ('cat','dog','man','call')
a,b,c,d = tup1
print(a,b,c,d)

#### Note : The number of variables must be equal to the number of items of the tuple.

######### Adding New Element in Tuple ###################
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple


###Q2) Write a Python program to add an item in a tuple.
####Soln: 
tup = (1,2,3,4)
tup = tup + (9,)
print(tup)

## Adding Items in Specific Index
tup = tup[:3] + (5,6,7) + tup[3:]
print(tup)

### Adding Items in tuple using append by converting them into list: 
list1 = list(tup)
print(list1)
list1.append(10) ## Append 
print(list1)
tup1 = tuple(list1) ### Converting List into Tuple
print(tup1)

############## Tuple To String ##################################
###Q3) Write a Python program to convert a tuple to a string.
####Soln: 
tup = ('e','n','d')
tup = "".join(tup)
print(tup)


###Q4) Write a Python program to get the 4th element and 4th element from last of a tuple.
### Soln: 
tup = ('e','l','e','p','h','a','n','t')
print(tup[3],tup[-4])

########### Removing Element from Tuple ############ Ways: 
## 1) Slicing : 
#create a tuple
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)

## 2) Using Remove: 
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)

###### Slicing the Tuple ############ 
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
print(_slice)
#if neither is defined, returns the full tuple
_slice = tuplex[:]
print(_slice)
#when step is negative the jump is made back
_slice = tuplex[9:2:-4]
print(_slice)

##### To Find Index of Tuple Element ############
### Syntax : tuple.index(value)
### Soln: 
tup = ('e','l','e','p','h','a','n','t')
# for i,v in enumerate(tup): 
#     print(i,v)
# for i in range(0,len(tup)): 
#     print(i)
print(tup.index('p')) 
print(tup.index('p',2))  ## Search Index starts from 2(e)
print(tup.index('n',2,7)) ### Search Index between 2(e) to 7(t)

### To Get Length of Tuple : 
print(len(tup))

#### Tuple to Dictionary ######## 
##Q3) Write a Python program to convert a tuple to a dictionary.
### Soln: 
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

#### Unzip List of Tupples 
##Q4) Write a Python program to unzip a list of tuples into individual lists.
### Soln: 
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l))) ## *l --> Unpacking list of tuple and then zipping them ---> list is used to generate the list of zipped tuple

################# Reversing the String #################################
## 1) Using Negative Index Slicing: 
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(tuplex[::-1])

## 2) Reversed: 
x = ("w3resource")
y = reversed(x)
print(tuple(y))


############  Set Default ##############
## Defination : The setdefault() method returns the value of the item with the specified key.
## Syntax : dictionary.setdefault(keyname, value)
## e.g : 
d = {'car':'tata','color':'black','year':1998}
print(d.setdefault('car'))

## Q5) Write a Python program to convert a list of tuples into a dictionary.
## Soln: 
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)


######## String Formatting ############
## Q6) Write a Python program to print a tuple with string formatting.
### Soln: 
tup = (100, 200, 300)
x = (10,20)
print('This is a tuple {0} and {1}'.format(tup,x))



#############List Comprehension in Tuple##################
func = [x+y for x, y in [(1,2),(3,4),(5,6)]]
print(func)