### Date & Time : https://www.w3resource.com/python-exercises/date-time-exercise/index.php

### Iterate over dates: 
import datetime 

## The size of each step in days 
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7*day_delta 

for i in range((end_date - start_date).days): 
    print(start_date + i*day_delta)
print(i*day_delta)
print((end_date - start_date).days)
############################################################

###Q1)Write a Python script to display the various Date Time formats.
#### Soln: 
import time 
import datetime 
print("Current Date and Time: ",datetime.datetime.now())
print("Current Year: ",datetime.date.today().strftime("%Y"))
print("Current Month: ",datetime.date.today().strftime("%B"))
print("Week Number of the Year: ",datetime.date.today().strftime("%W"))
print("Weekday of the Year: ",datetime.date.today().strftime("%w"))
print("Day of the Year: ",datetime.date.today().strftime("%j"))
print("Day of the Month: ",datetime.date.today().strftime("%d"))
print("Day of the Week: ",datetime.date.today().strftime("%A"))

###Q2)Write a Python program to determine whether a given year is a leap year.
#### Soln: 
def leap_year(y): 
    if y % 400 == 0: 
        return True
        # print("{} is a leap year".format(y))
    if y%100 == 0: 
        return False
        # print("{} is not a leap year".format(y))
    if y % 4 == 0: 
        return True
        # print("{} is a leap year".format(y))
    else: 
        return False
        # print("{} is not a leap year".format(y))
print(leap_year(1900))
print(leap_year(2004))

###Q3)Write a Python program to convert a string to datetime.
#### Soln: 
# import time 
# import datetime 
from datetime import datetime
date_object = datetime.strptime('Mar 21 2022 11:12AM', '%b %d %Y %I:%M%p')
date_obj = datetime.strptime('March 22 22 1:12', '%B %d %y %H:%M%p')
print(date_object)
print(date_obj)
#####################-----------------------------------######################
### Note: 
# %b --> Short version of Month (eg. Mar)
# %d --> day
# %Y --> Full year (YYYY-2022)
# %y --> Short year(YY-22)
# %I --> Hours in 12hr format(0-11)
# %M --> Min 
# %p --> AM/PM
#####################-----------------------------------######################

#### -------> To Get Current Data n Time: 
###Q4)Write a Python program to get the current time in Python.
#### Soln: 
# import time 
# import datetime 
from datetime import datetime
curr_time = datetime.now()
print(curr_time)

### -----> Subtracting Days from Current Date : 
###Q5) Write a Python program to subtract five days from current date.
#### Soln: 
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

### Q6) Write a Python program to print yesterday, today, tomorrow.
#### Soln: 
from datetime import date,timedelta 
today = date.today()
yestr =  date.today() - timedelta(1)
next_day = date.today() + timedelta(1)
print("Current Date: ",today)
print("Yesterday Date: ",yestr)
print("Tomorrow Date: ",next_day)

### Q7) Write a Python program to convert the date to datetime (midnight of the date) in Python.
#### Soln: 
from datetime import date 
from datetime import datetime 
today = date.today()
print(datetime.combine(today,datetime.min.time()))


### Q8) Write a Python program to print next 5 days starting from today.
#### Soln: 

import datetime 
base = datetime.datetime.today()
for x in range(0,5): 
    print(base + datetime.timedelta(days=x))


### Q9)Write a Python program to add 5 seconds with the current time.
#### Soln: 
import datetime 
x = datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())


### Q10) Write a Python program to calculate an age in year.
#### Soln: 
from datetime import date

def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
print()
print(calculate_age(date(1991,12,8)))
print(calculate_age(date(1989,4,30)))
print(calculate_age(date(1994,1,3)))
print(calculate_age(date(1995,6,28)))
print(calculate_age(date(2001,5,14)))
print()