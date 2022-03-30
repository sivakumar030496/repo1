"""1)Write a program to find the characters which matches with the keys of given dictionary and replace them with the associated value.
d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
Input: abc
Output: bca"""



d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
g = ['a','b','c']
for g in d:
    print(d.get(g))


"""2)Write a program to print the factorial of a given number using a while loop. Don't use any predefined or user-defined functions"""


n = int(input("enter the numer:"))
fact = 1
while(n>=0):
    fact=fact*n
    n = n - 1
    print("factorial of the number is: ")
    print(fact)
"""3)Write a Python program to get the maximum and minimum value from a list without using any predefined function"""

list = [1,2,3,4,5,5,6,7,8,8,9]

print(max(list))
print(min(list))

"""4)Define a list that contains the marks percentage for the students. Print a list that contains the Grades of the students.
  The grading will be decided by the following conditions.
  A+ if the percentage is greater than 90
  A if the percentage is less than or equal to 90 and greater than 70
  B if the percentage is less than or equal to 70 and greater than 50
  C if the percentage is less than or equal to 50 and greater than 35
  F if the percentage is less than or equal to 35"""

marks = int(input("enter of the student marks:"))
persentage=(marks/600)*100
print("persentage of marks",persentage)
if(100>persentage>90):
    print("grade: A+")
if(90>persentage>70):
    print("grade: A")
if(70>persentage>50):
    print("grade: B+")
if(50>persentage>35):
   print("grade: b")

else:
    print("grade: d")




"""5)Print the type of integer until the given index position in characters(Even or Odd) exclude index 0.
Input: [0,1,2,3,4,6,7,8]
index: 5
Output: ['Odd','Even', 'Odd', 'Even', 'Even']"""


x=[0,1,2,3,4,6,7,8]
l = []
for i in x[1:5]:
    if i%2==0:
        l.append("even")
    else:
        l.append("add")
print(l)




"""6)Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if the limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20."""

s=0
for i in range(21):
    if  (i%5==0 or  i%3==0):
        n=s+i
        print(n) 

"""7)Write a program to print the following:
*
**
***
****
*****"""

for i in range(5):
    for j in range(i+1):
        print("*",end= "")
    print()

"""8)Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""

n = "fizzbuzz"
if "fizzbuzz" in n:
 for fizzbuzz in range (6):
    if (fizzbuzz%5==0) or (fizzbuzz%3==0):
        print(fizzbuzz)
        continue
    if(fizzbuzz%3==0):

        print("fizz")
        continue
    if(fizzbuzz%5==0):
        print("buzz")
        continue
    print("fizzbuzz")

""""9)Write a program to reverse a string word by word along with reverse the characters in each word."""

string = input("enter the string:")
rev_string=string[::-1]
print("string is elephant",rev_string.split())

"""10)Define a list and create a dictionary where the dictionary key is an index of the element and value
is an element in the lis"""

data = {1:'tamilnadu',2:'andrapradesh',3:'telengana',4:'delhi'}
hostel={}
hostel["day1"]=25
hostel["day2"]=87.6
hostel["day3"]=123.2
hostel["day4"]=145
print(data)
print(hostel)
print(data.get(1))
print(data.get(2))
print(data.get(3))
print(data.keys())
print(data.values())

"""1)Write a simple Python function to check whether x is even or odd"""

num = 3
if (num % 2)==0:
    print("{0} is even number".format(num))
else:
    print("{0} is odd number". format(num))


"""2)Write a function to tell the user if he/she is able to vote or not.
 ( Consider minimum age of voting to be 18. )"""

age = int(input("enter the age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")




"""3)Write a function “perfect()” that determines if the parameter number is a perfect number. 
Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
[An integer number is said to be a “perfect number” if its factors, including 1(but not the number itself), 
sum to the number. E.g., 6 is a perfect number because 6=1+2+3]"""


lower = int(input("enter the lower limit: "))
upper = int(input("enter the upper limit: "))
for num in range(lower,upper+1):
    sum = 0
    for i in range (1,num):
        if (num%i)==0:
            sum=sum+i
    if num==sum:
        print(num)


"""4)Write a function that takes a list as input param and it returns two lists one with even, one with odd values use the lambda function."""

even = [23,4,5,34,245,76,78,88]
list = list(filter(lambda even: even>=18 , even))
print(list)

"""5)Write a function that takes a list as input and returns a new list by multiplying all the elements from the given list with 10."""

mylist = [ 2,5,6]
result=1
for i in mylist:
    result=result * 10
    print(result)


"""6)Write a function to print the factorial of a number."""

n = int(input("enter the number:"))
result = 10
for i in range (n,0,-1):
    result=result*i
print("factorial of",n,result)


##second metod##
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter the number:"))
result=fact(n)
print("factorial if",n,"is",result)



"""7)Write a function to check whether the given year is a leap year or not."""

year = int(input("enter a year:"))
if (year % 4 ) == 0:
    if (year % 100 ) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0] is not a leap year".format(year))



"""8)Write a function to pass dynamic args and return the sum of the dynamic args."""

def mycollegedays(*argv):
    for arg in argv:
        print(arg)

mycollegedays("welcome","to","chennai")

"""9)Write a function to pass keyword args and update the dictionary"""

dict1 ={1:"siva",2:"pawan"}
list1=[3,"s"]
dict1.update([list1])
print(dict1)

dict1.update(d=3,h=4,t=3)
print(dict1)

dict2={6:"chennai"}
dict1.update(dict2)
print(dict1)

"""10)Write a function to print the following
*
**
***
****
*****
****
***
**
*"""

n = 1
f1 = False
while n>=1:
    print(n* "*")
    if n==5:
      f1=True
    if f1:
       n=n-1
    else:
       n=n+1

































