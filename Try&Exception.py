### Try/Exception: 
## Qn : Raise ZeroDivisionError 
## Soln1: 
try:
    print(25 % 0)
except Exception as e: 
    print("Zero!")
    
## Soln2: 
try:
    print(25 % 0)
except ZeroDivisionError:
    print("Zero!")
    
## Qn: Try raises no exception then program prints out result and string Clean!.
## Soln: 
try:
    print(25 % 5 ** 5 + 5)
except:
    print("Bug!")
finally:  ## else: 
    print("Clean!")

## Code 
try:
    print(25 % 5 ** 5 + 5)
except ZeroDivisionError: 
    print("Zero!")
else: 
    print("Clean!")
finally: 
    print("Finish!")
    
## Code: 
x = [1, 9, 17, 32]
 
try:
    print(x[3] % 3 ** 5 + x[4])
except ZeroDivisionError:
    print("Zero!")
except IndexError:
    print("Index!")