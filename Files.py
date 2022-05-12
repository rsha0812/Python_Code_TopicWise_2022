### Files: --- Source : Udemy 
### All commands avaialble in Udemy Cheat Sheet.  


## Qn: To read the content of the file as string: 
## Soln: 
f = open("test.txt", "r")
print(f.read())

## Qn: To read content of the file as a list,where each element of teh list is a row in the file  
## Soln: 
f = open("test.txt", "r")
print(f.readlines())

## Qn: To bring the cursor at very beginning of teh file before reading the file again. 
## Soln: 
f = open("test.txt", "r")
f.read()
f.seek(0)
print(f.read())

## Qn: To get the current position of the cursor. 
## Soln: 
f = open("test.txt", "r")
f.read(5)
print(f.tell())

## Qn: To get the current mode of the file.
## Soln: 
f = open("test.txt", "r")
f.read(5)
print(f.mode)

## Qn: To open .txt file for appending & reading at the same time. 
## Soln: 
f = open("test.txt","a+" )
print(f.mode)

## Qn: To write the "python" to .txt file and have the result of reading the file printed out to the screen. 
## Soln: 
f = open("test.txt", "w")
f.write("python")
f.close()
f = open("test.txt", "r")
print(f.read())

## Qn: To write list of string ['python','','and','','java'] to .txt. 
## Soln: 
f = open("test.txt", "w")
f.writelines(['python',' ','and',' ','java'])
f.close()
f = open("test.txt", "r")
print(f.read())

## Qn: To write a string "python" in test.txt file and close it suing with statement.
### Soln: 
with open('test.txt','w') as f: 
    f.write("python")
f.close()
f = open("test.txt", "r")
print(f.read())

## Qn: To delete entire content of the file.
## Soln: 
with open("test.txt", "w") as f:
    f.write("python")
f = open("test.txt","r+") ## the file should be open for reading AND writing
f.truncate() ## Delete all data 
## f.truncate(10) ## leave first 10 character of file and delete rest
f = open("test.txt", "r")