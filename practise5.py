"""1) Write a program to print the following into a text file.
*
**
***
****
*****
****
***
**"""




"""2)Write a python program with buggy code and add a try/except clause so the code runs without errors."""


import math
num = int(input("please enter the number to calculate factorial:"))
try:
     result=math.factorial(num)
     print(result)
except:
     print("cannot compute the factorial of negative number")

"""3)Write a python program to demonstrate different kinds of predefined exceptions."""








"""7)Write a Python program to count the frequency of words in a file."""

from collections import counter
def word_count(fname):
     with open (fname)  as f:
          return counter(f.read().split())
     
print("number of words in the file :",word_count("test.txt"))


"""8)Write a Python program to append 'El Niño' string to the text file using encoding."""

x ='El Niño'
f=open('demo.txt','wb')
code=x.encode('utf-8')
f.write(code)

"""16) Write a Python program to multiply all the items in a dictionary"""

s = {'a':30,'b':40,'c':12}
count = 1
for i in s:
    count=count*s[i]
print(count)


"""17)Write a Python program to get the maximum and minimum value in a dictionary"""

s = {'a':30,'b':23,'c':65,'d':67}
key_max=max(s.keys(),key=(lambda k: s[k]))
key_min=min(s.keys(),key=(lambda k: s[k]))
print('maximum values: ',s[key_max])
print('minimum values: ',s[key_min])


"""18)Read 3 numbers and print them in sorted order."""

x = 1
y = 2
z = 3
a1 = min(x,y,z)
a3 = max(x,y,z)
a2 = (x+y+z)-a1-a3
print("numbers in stored order: " ,a1,a2,a3)


