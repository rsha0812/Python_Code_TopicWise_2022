## Code1 : OverRiding Variable
a = 2
a = 4
a = 6
print(a + a + a)
''' 
Explanation: Since Python reads and executes scripts from top to bottom, variable a  will be updated in every line until line 3 
where a  finally gets the value of 6 . Then the print  function prints out 6 + 6 + 6  which is 18 .'''

## Code2: Naming Rules 
a = 1
_a = 2
_a2 = 3
2a = 4 ## This will Throw Error
print(_a2)
''' 
Explanation: 
Variable names must start with a letter or an underscore. Everything else will throw a SyntaxError.'''

## Code3: Compare vs Assign
a = 1 ## "=" is assignment operator
b = 2
print(a == b) ## False - Here "=" is a comparison operator
print(b == c) ## NameError: name 'c' is not defined As we are not assigning c equals to b but we comparing c with b.

## Code4: Creating list from range(1,20) ---- List
## Using List Comprehension:
lst = [i for i in range(1,21)]
print(lst) ## O/P : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
## Using range
my_range = range(1, 21)
print(list(my_range)) ## O/P : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

## Multiplying Each element of list with 10: 
lst = [i*10 for i in range(1,21)]
print(lst) ## O/P : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

## Converting int-datatype of element of List into string: 
print(list(map(str,my_range))) ## O/P : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']


## Code5 : Create Dictionary that contains key : a & b and values : 1 & 2.  ---- Dictionary
## Method 1: 
d = {"a": 1, "b": 2} ## Using curly brackets is one way to create a dictionary.
## Method 2: 
d = dict(a = 1, b = 2) ## A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.

### Adding two values of Dictionary: 
d = {"a": 1, "b": 2,"c":3}
print(d["a"] + d["b"])
d.update({"c":4}) ## Updating same key with different value will override teh value.
d["d"] = 5 ## Another way of updating key value pair in dictionary
print(d)

### Filtering/removing Value greater than 1.
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

### Creating Dictionary using range():
from pprint import pprint
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)

''' Note: 
We're using ranges here to construct the lists. 
We're also using the built-in Python pprint  module, which is used to print out well-formatted views of datatypes in Python.'''

### Accessing Values from Nested Dictionary: 
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
         
print(d['employees'][1]['lastName'])
d['employees'][1]['lastName'] = "Smooth"  ### To change last name from smith to smooth.
d["employees"].append(dict(firstName = "Albert", lastName = "Bert")) ### To add new employee details in dict
print(d)
'''
Explanation:
d['employees']  returns this list:
[{"firstName": "John", "lastName": "Doe"},
 {"firstName": "Anna", "lastName": "Smith"},
 {"firstName": "Peter", "lastName": "Jones"}]
d['employees'][1]  returns the second item of the above list:
{"firstName": "Anna", "lastName": "Smith"}
And finally d['employees'][1]['lastName']  returns the value of lastName :
Smith ---O/p '''

### Storing Dictionary to Json File: 
import json
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
with open("company1.json", "w") as file:
    json.dump(d, file, indent=4)

#### Json to Dictionary : 
import json
from pprint import pprint
with open("company1.json","r") as file:
    d = json.loads(file.read())
pprint(d)

### Add anew employee to the json file: 
import json
with open("company.json","r+") as file:  ## r+ --> read & write mode
	d = json.loads(file.read())
	d["employees"].append(dict(firstName = "Albert",lastName = "Bert"))
	file.seek(0) # to keep cursor at first line(Top of the file)
	json.dump(d,file,indent = 4, sort_keys = True) ## 
	file.truncate() ## this remove the old dictionary.
## MultiIndexing : To fetch 13 from key ='b' second value 
from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d['b'][2])


### Code6 : Make a script that prints out letters of the English alphabet from a to z, one letter per line in the terminal.
import string
for letter in string.ascii_lowercase:
    print(letter)

 ''' Note: string  is a built-in module and string.ascii_lowercase  returns a string object containing all 26 letters of the English alphabet. 
 Then we simply iterate through that string and print out the string items.'''


 

### Code7: Local and Global Variable: 
c = 1 ## Global Variable 
def foo():
	c = 2
    return c ## Local Variable 
c = 3 ## Global Variable 
print(foo()) ## O/p : 2


### Code8 : Create a function that takes text file as input and return the count of words in text file.  ----- Word Count(Reading Files)
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("words1.txt"))

#### Removing (,) from str to split: 
def count_words(file):
    text = file.replace(",", " ")
    print(text)
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("A tree is a woody perennial plant,typically with branches."))

### Word Count using File and writing above code: 
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("words2.txt"))

### Code9: Create a script that generates a text file with all english alphabet inside the file, one letter per line.  ---- Writing File 
import string
with open("letters.txt", "w") as file: ## Opening file in write mode
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")

## Creating file where each line has only two alphabet. (ab,cd,ef ..so on in each line)
import string 
with open("string_letter.txt","w") as file:
    for l1,l2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]): 
        file.write(l1 + l2 + \n)

### Code10: Adding Element of List & Tuple. --- Zip(Imp)
a = [1, 2, 3]
b = (4, 5, 6)
for i,j in zip(a,b): 
    print(i+j)


#### Code 11: Create a script that iterates through text files and 
###checks if strings p, y, t, h, o, or n are found in the text file's content. If any of those strings is found, append that string to a list.
import glob
 
letters = []
file_list = glob.iglob("letters/*.txt") ## letter is a folder that has 26 text file 
check = "python" ## checking if python is available in file or not 
 
for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
    if letter in check:
        letters.append(letter)
print(letters)

'''
Note : The glob module here helps to generate a list of text files. Then we iterate through that list and read each file inside the loop, 
strip "\n" characters and then check if the letter extracted from the file is in the string "python," and we append that letter if it is.'''