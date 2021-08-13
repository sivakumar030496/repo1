"""1)Write a Python program to get the number of occurences of the given character in overall dictionary.
 d = {1:['a', 'G', 'k', 'l'], 2:['G', 'b', 'c'], 3:['a', 'k', 'G', 'c']}
Input: G
Output: 3"""

x = "welcometochennai"
count = 0
for i in x:
    if i == 'e':
        count=count+1
print("count of tallent: " + str(count))

"""2)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Input : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Output : ['Green', 'White', 'Black']"""


color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color =[x for (i,x) in enumerate(color) if i in (0,4,5)]
print(color)

"""3)Write a program to count the number of strings where the string length is 2 or more and the first 
and the last characters are the same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result: """

def math_words(words):
    count=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count +=1
    return count
print(math_words(['abc', 'xyz', 'aba', '1221']))

"""4)Write a Python program to count the number of characters (character frequency) in a string
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""

def count(string):
    output={}
    for i in string:
        keys=output.keys()
        if i not in keys:
            output[i]=+1
        else:
            output[i]=1
    return output
print(count("google.com"))

"""5) Create a new dictionary by extracting the following keys from a given dictionary.
d = {"name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}
Keys to extract:
keys = ["name", "salary"]
Output: {'name': 'Kelly', 'salary': 8000}"""

d = {"name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}
print("the original dictionary is: "+str(d))
res={key: d[key] for key in d.keys()
     &{'name','salary'}}
print("the filtered dictionary is: " + str(res))

"""6)Define a dictionary and a number and verify that the number exist in dictionary values or not. 
The output should be True or False"""

d = {1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print("key is present in the dictionary")
    else:
        print("key is not present in the dictionary")
is_key_present(5)
is_key_present(9)

"""7)Write a Python program to sum all the items in a list."""

def list(items):
    sum_numbers=0
    for i in items:
        sum_numbers=+i
    return sum_numbers
print(list([1,2,-5]))



"""8)Write a Python program to remove duplicates from a list."""

a = [10,20,30,40,40,50,50,60,60,70,70,80]

dup=set()
uniq=[]
for i in a:
    if i not in dup:
        uniq.append(i)
        dup.add(i)
print(dup)


"""9)Write a Python program to multiply all the values in a dictionary where all the values are integers."""

d={'a':1,'b':2,'c':3,'d':4}
result=1
for i in d:
    result=result*d[i]
print(result)

"""10)Write a program to demonstrate difference b/w discard and remove methods on a set"""

def remove(sets):
    sets.discard(20)
    print(sets)
sets=set([10,10,20,30,40,50,60,70])
remove(sets)

"""11)Define n and print n natural numbers using a while loop."""

num = int(input("enter the natural numbers:"))
i=1
while i<=num:
    print(i)
    i=i+1

"""12)Print multiplication table of a given number"""

num=int(input(("enter the number:")))
for i in range(1,21):
    print(num,'x',i,'=',num*i)

"""13)Given a list iterate it and display numbers that are divisible by 5 and if you find a number 
greater than 150 stop the loop iteration
Ex: Input: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
Output: 15
55
75
150"""

list=[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list:
    if i%5==0:
      if i<= 150:
          print(i)

"""14)Reverse the following list using for loop."""

list=(9,8,7,6,5,4,3,2,1,0)
for i in reversed(list):
    print(i)


"""15)Write a loop to find the factorial of any number"""

num = int(input("The factorial number :"))
fac = 1
for i in range(1,num,+1):
    fac = fac *i
print("factorial of",num,"is",fac)

"""while loop method"""

num = int(input("factorial number:"))
fac=1
i=1
while i<=num:
    fac=fac*i
    i =i+1
print("factorial of",num,"is",fac)

"""16)Use a loop to find elements from a given list that are present at even positions.
Input: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Output: [20, 40, 60, 80, 100]"""

list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lst=[]
for i in range(1, len(list), 2):
    lst.append(list[i])
print(lst)

"""17)Find the length of the given number without using len().
Input: 123
Output """

n = (1,2,3)
count = 0
for i in n:
    count=count+1
print("given number",count)

"""18)Access the value of key ‘history’ from the following dict.
{ 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}"""

d = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print(d['class'],['student'],['marks'],['history'])


"""19)Given two integer numbers return their product and  if the product is greater than 1000, then return their sum"""
x = int(input("enter the number"))
y = int(input("enter the number"))
z = x*y
a = x+y
print(a)

"""20)Given a string, display only those characters which are present at an even index number"""

for index in range(len(str)):
    if index % 5==0:
        print(str[index], end='')




