# """decarators method"""
# from abc import ABC,abstractmethod
# class abstractdemo(ABC):
#     @abstractmethod
#     def display(self):
#         None
#     @abstractmethod
#     def show(self):
#         None
# class demo(abstractdemo):
#     def display(self):
#         print('ABSTRCT METHOD')
# class demo1(abstractdemo):
#     def show(self):
#         print('SHOW METHOD')
#     def display(self):
#         print('DISPLAY METHOD')
# obj=demo1()
# obj.show()
# obj.display()

#@property
# class student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     @property
#     def display(self):
#         return self.name+" got grade "+self.grade
# s1=student('siva','A')
# print(s1.name)
# print(s1.grade)
# print(s1.display)


# class Student:
#     name='siva' #class attribute
#     def __init__(self):
#         self.age=20 #instance attribute
#     @staticmethod
#     def display():
#         print("STUDENT CLASS")
# stu=Student()
# stu.display()
# Student().display()

# class student:
#     name='siva'
#     def __init__(self):
#         self.age=24
#     @classmethod
#     def display(cls):
#         print('name=',cls.name)
# stu=student()
# stu.display()
# student().display()
#
# """febbinacci"""
# n=int(input("Enter the number how many series:"))
# first=0
# second=1
# for i in range(n):
#     print(first)
#     temp=first
#     first=second
#     second=temp+second
#
# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         c=a
#         a=b
#         b=c+b
# fib(10)

#
# """compare 2 dictionaries and eliminate duplicate keys and concatenate to one"""
# def merge(dict1,dict2):
#     return dict2.update(dict1)
# dict1={'a':10,'b':20}
# dict2={'c':30,'d':40}
# print(merge(dict1,dict2))
# print(dict2)


# def merge(dict1,dict2):
#     res=dict1 | dict2
#     return res
# dict1={'a':10,'b':8}
# dict2={'d':30,'c':14}
# dict3=merge(dict1,dict2)
# print(dict3)
#
# """14)split the time to hh:mm:ss"""
# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%X"))
# print(x.strftime("%x"))
#
# """13)date to str and str to date"""
#
# now=datetime.now()
# datetime=now.strftime("%m/%d/%y")
# print(datetime)
#
# date_str='07-22-2021'
# date_object=datetime.strip("%m/%d/%y")
# print(datetime)
#
# import datetime
# print ('Current date/time: {}'.format(datetime.datetime.now()))
#
# x=datetime.datetime(2021,7,22)
# print(x.strftime("%B"))
# print(x.strftime("%A"))

"""multithreading"""

# from time import sleep
# from threading import *
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
# t1=Hello()
# t2=Hi()
# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print('Bye')
#
# #reverse a string witout using slicing
# s='siva'
# n=" "
# for i in s:
#     n=i+n
# print(n)
#
# #using reverse join method
#
# s='siva'
# string=''.join(reversed(s))
# print(string)
#
# #using slicing in reverse method
#
# s='siva'
# len=len(s)
# string=s[len::-1]
# print(string)
#
# def fun(x):
#     return x[::-1]
# y=fun('siva')
# print(y)
#
# s=input()
# for i in range(len(s) -1,-1,-1):
#     print(s[i],end="")
# print("\n")
#
# #program to define the whether a number is a prime
#
# n=int(input("Enter the number:"))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count=i+1
# if count>1:
#     print(count,'This is not a prime numer')
# else:
#     print(count,'This is a prime number')
#
# #only prime numbers
# for num in range(1,101):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:

#             print(num)
#
#
# noprime=[j for i in range(2,8)for j in range(i*2,100,i)]
# prime=[x for x in range(2,100) if x not in noprime]
# print(prime)
#
# # even or odd number
# n=int(input("Enter the number:"))
# if  n%2==0:
#     print(n,'is a even number')
# else:
#     print(n,'is a odd number')

# s=[1,2,3,4,5,6,7,8,9,10]
# n=[]
# for i in s:
#     if i%2==0:
#         n.append(i)
#    print(n)

#
# #normal inheritance
#
# class baseclass:
#     a=10
#     b=100
#     def display(self):
#         print("BASE CLASS")
# class derivedclass:
#     c=20
#     d=200
#     def show(self):
#         print("DERIVED CLASS")
# bobj=baseclass()
# print(bobj.a,bobj.b)
# bobj.display()
# dobj=derivedclass()
# print(dobj.c,dobj.d)
# dobj.show()

 # single inhritance
#
# class Baseclass:
#     a=10
#     b=100
#     def display(self):
#         print("BASE CLASS")
# class Derivedclass(Baseclass):
#     c=20
#     d=200
#     def show(self):
#         print("DERIVED CLASS")
# dobj=Derivedclass()
# print(dobj.c,dobj.d)
# dobj.show()
# bobj=Baseclass()
# print(bobj.a,bobj.b)
# bobj.display()
#
# # multilevel inheritance
#
# class grandparent:
#     def gpdispaly(self):
#         print("GRAND PARENT METHOD")
# class parent(grandparent):
#     def pdisplay(self):
#         print("PARENT METHOD")
# class child(parent):
#     def cdisplay(self):
#         print("CHILD DISPLAY")
# c=child()
# c.gpdispaly()
# c.pdisplay()
# c.cdisplay()
#
# #multiple inheritance
# class father:
#     def fdisplay(self):
#         print("FATHER CLASS")
# class mother:
#     def mdisplay(self):
#         print("MOTHER CLASS")
# class child(father,mother):
#     def cdisplay(self):
#         print("CHILD CLASS")
# c=child()
# c.cdisplay()
# c.fdisplay()
# c.mdisplay()
#
# #hirarchical inheritance
#
# class parent:
#     def pdisplay(self):
#         print("PARENT CLASS")
# class son(parent):
#     def sdisplay(self):
#         print("SON CLASS")
# class daughter(parent):
#     def ddisplay(self):
#         print("DAUGHTER CLASS")
# s=son()
# s.pdisplay()
# s.sdisplay()
# d=daughter()
# d.pdisplay()
# d.ddisplay()
#
# #public,protected,private
# class person:
#     def __init__(self,name,age,height):
#         self.name=name                 #public
#         self._age=age                  #protected
#         self.__height=height           #private
# p1=person("siva",24,172)
# print(p1.name)        # public: can be accessed
# print(p1._age)        # protected: can be accessed but not advised
#  print(p1.__height)  # private: will give AttributeError
#
# """print(p1.__height). You will notice it gives an AttributeError since you cannot access a private class member outside the class."""
#
# #private
# class person:
#     # def __init__(self,name,age,height):
#     name="shiva"
#     _age=24
#     __height=172
#     @classmethod
#     def gang(cls):
#         print(cls.__height)
#         print(cls._age)
# p1=person()
# print(p1.name)
# print(p1.gang())
#
# """Python program to print the duplicate elements of an array"""

# l=[1,1,2,3,3,4,5]
# print(set(l))
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             print(l[j])
#
# """"convert to string in abcd add the out put a:1 ,b:1,c:1,d:1"""
# x='abcd'
# y={}
# for i in x:
#     if i not in y:
#         y[i]=1
# print(y)
#
# l='asdfghj'
# d={}
# var=1
# for i in l:
#         d[i]=1
#         var+=1
# print(d)

# input='abcd'
# d={}
# for i in range(len(input)):
#     d.update({input[i]:i+1})
# print(d)


# """ will we take of function convert to type coasting take a decorator and print the 2 strings """
# """in put ('siva','kumar')"""
# """out put= siva kumar """
# def concatination_string(func):
#     def inner(a,b):
#         if type(a)==str and type(b)==str:
#             return func(a,b)
#         else:
#             print('concatination is possible')
#     return inner
# @concatination_string
# def string(a,b):
#     return a+b
# print(string('siva','kumar'))


#List Comprehension

# j=[x for x in range(20) if x%2==0]
# print(j)


#
# y=[u for u in range(100) if u%2==0 if u%5==0]
# print(y)
#
# l=[[1,2],[3,4],[5,6],[7,8]]
# l1=[[row[i] for row in l] for i in range(2)]
# print(l1)

# a=201
# b=[x for x in range(2,a) if all(x % y !=0 for y in range(2,x))]
# print(b)


# """get int element from the srting"""
# s='siva 1 papaiahgari 2'
# n=[]
# for i in s:
#     if i.isdigit():
#         n.append(i)
# print(n)
#
# """get string element from the integer"""
# s='siva 1 papaiahgari 2'
# n=[]
# for i in s:
#     if i.isalpha():
#         n.append(i)
# print(n)

# """input=[1,2,3,4,5]"""
# """out put=[1,2,3,4,5,6]"""
# a=[1,2,3,4,5]
# def list(a):
#     b=a+[6]
#     print(b)
# list(a)
#
# l=[1,2,3,4,5]
# l1=[6]
# n=l+l1
# print(n)

# """input='my name is siva'"""
# """out put= siva is my name"""

# s='my name is siva'
# n=" "
# for i in s.split():
#     n=i+" "+n
# print(n)

# no_prime=[j for i in range(2,8)for j in range(i*2,101,i)]
# print(no_prime)
# prime_no=[x for x in range(2,101)if x not in no_prime]
# print(prime_no)

#
# def lowercase(fun):
#     def inner(a):
#         if a.islower():
#             return fun(a)
#         else:
#             print("invalid keyword")
#     return inner
# @lowercase
# def string(a):
#     print(a.upper())
# string('CHENNAI')

# l=[1,2,3,'siva','sasi']
# s=[x for x in l if type(x) in [int]]
# n=[x for x in l if type(x) == str]
# print(s)
# print(n)

# l=[1,2,3,"bhanu","siva"]
# c=[]
# s=[]
# for i in l:
#     if type(i)== int:
#        c.append(i)
#
#     elif type(i)==str:
#         s.append(i)
# print(c)
# print(s)

# c=[i for i in l if type(i) in [int]]
# d=[j for j in l if type(j)==str]
# print(c)
# print(d)

# d=[{"V":"S001"},{"V":"S002"},{"VI":"S003"},{"VI":"S004"}]
# l=[]
# for i in d:
#     for k,v in i.items():
#         l.append(v)
# print(l)

# l=[1,2,3,4,5]
# count=0
# for i in l:
#     count=count+int(i)
# print(count)


# l=list(map(int,input("Enter array elements:").split(" ")))
# min1=l[0]
# for i in range(1,len(l)):
#     if(l[i]<min1):
#         min1=l[i]
# print(min1)

# l=[10,20,30,40,50,50,10,30]
# min=l[0]
# for i in range(len(l)):
#     if l[i]<min:
#         min=l[i]
# print(min)

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             print(l[j],end=" ")
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#        print(i,end=" ")

# import random
# x = random.sample(range(1,101), 100)
# print(x)

# l=[1,2,3,4,5,6]
# print(type(l))
# print(type("".join(map(str,l))))
# L = [1,2,3,4,5,6]
# n=(" ".join(map(str,L)))
# print(n)


# a=[1,2,3,4,5,6,7,8,9,10]
# b=[1,2,3,4,5]
# print(set(a).intersection(b))
# n=[x for x in a if x in b]
# print(n)


# print(a[1::2])

# def natural(n):
#     for i in range(1,n+1):
#         yield i
# natural(1000)
# for i in natural(1000):
#     print(i,end=" ")


# class person:
#     def __init__(self,name,age,height):
#         self.name=name
#         self._age=age
#         self.__height=height
# p1=person('siva',24,172)
# print(p1.name)
# print(p1._age)
# print(p1.__height)

# s = 'Hello world'
# d={}
# for i in s:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# x=2+9*((3*12)-8)/10
# print(x)


#
# # print(l[:5])
# l=[1,2,3,4,5]
# s=[]
# for i in l:
#     s.insert(0,i)
# print(s)
# s=input().split(" ")
# s1=""
# l=[]
# for elem in s:
#     s1=elem+s1
#
# print(" ".join(l))

# s='my name is siva'
# n=''
# for i in s:
#     n=i+n
# p=""
# for elem in n.split(" "):
#     p=elem+" "+p
# print(p)

# s='this is a book'
# n=''
# for i in s:
#     n=i+n
# p=''
# for ele in n.split( ):
#     p=ele+" "+p
# print(p)
#
# def cubicvar():
#     i = 1
#     while True:
#         yield i+i+i
#
#         i += 1
#
# for num in cubicvar():
#     if num > 1000:
#         break
#     print(num,end=" ")


# for i in range(1,101):
    # for j in range(2,i):
    #     if i%j==0:
    #         break
    # else:
    #
    #     print(i,end=" ")
# n=100
# a=[x for x in range(2,n) if all(x%y!=0 for y  in range(2,x))]
# print(a)

# x=['ab','cd']
# y=list(map(list,x))
# print(y)
# import pandas as pd
# import pandas as ps
# l=[1,2,3,4]
# l1=pd.Series(l,index=['i','ii','iii','iiii'])
# print(l1)
# d={'name':['siva','venkey','mahesh'],'persentages':[12,34,56]}
# d1=pd.DataFrame(d)
# print(d1)
# str = input('enter value :')
# s = str.split()
# s.sort()
# print(s)


#
# s='country'
# print(s[2::]+'oc')

# l=['chennai','benglore','hydrabad','coimbatore']
# l1=[x for x in l if 'a' in x]
# print(l1)

# import pandas as pd
# l=[1,2,3,4,5]
# l1=pd.Series(l)
# print(l1)
# l2=pd.Series(l,index=['i','ii','iii','iv','v'])
# print(l2)
# d={'name':['siva','sasi','prasad'],'persentage':[12,34,56]}
# l3=pd.DataFrame(d)
# print(l3)

# s=pd.Series()
# print(s)

# data={'a':0.,'b':1.,'c':2.}
# s=pd.Series(data,index=['b','c','d','a'])
# print(s)
#
#
# d=pd.DataFrame{(['Andrapradesh','Maharashtra','Karnataka','Kerala','Tamil Nadu']
#                 ,['Vijayawada','Mumbai','Bengaluru','Trivendrum','Chennai'],d,columns=['State','Capital']}
#
#
#
# data={'name':['siva','sasi','prasad','bhanu'],'Age':[23,45,43,67]}
# d=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
# print(d)


# l=list(map(int,input("Enter array elements:").split(" ")))
# min1=l[0]
# for i in range(1,len(l)):
#     if(l[i]<min1):
#         min1=l[i]
# print(min1)
#
# l=list(map(int,input("Enter array elements:").split(" ")))
# e=int(input("Enter a number:"))
# for i in range(0,len(l)):
#     if(l[i]<e):
#         print(l[i],end=" ")

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,0]
# l1.extend(l2)
# m=2
# for i in l1:
#     if m>i:
#
# class Human:
#     color="black"
#     height=5.57
#     def run(self):
#         print("RUNNING")
#     def walk(self):
#         print("WALKING")
# obj=Human()
# print(obj.color,obj.height)
# obj.run()
# obj.walk()

# a=20
# b=30
# if a<b and a>b:
#     print("a is less than b")
# else:
#     print("a is less than b")

# class Human:
#     def __init__(self):
#         print("Constructor")
#     def run(self):
#         print("RUNNING")
#     def walk(self):
#         print("WALKING")
# obj=Human()
# obj.run()
# obj.walk()
#
# class Human:
#     def __init__(self,c,h):
#         self.color=c
#         self.height=h
#     def run(self):
#         print("RINNING")
#     def walk(self):
#         print("WALKING")
# obj=Human()
# print("srikanth.white","srikanth.5.56")
# obj.run()
# obj.walk()

# string=input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

#
# ip_str = 'Hello, have you tried our tutorial section yet?'
#
# ip_str = ip_str.casefold()
# count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}
# print(count)
#
# ch = input("Enter the character : ")
#
# if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#
#   print("Vowel")

# s='my name is siva'
# n=''
# for i in s:
#     n=i+n
#     if n==0:
#         print('yes')
#     else:
#         print("no")

# txt = "The best things in life are free!"
# print("hre" not in txt)

# l=[10,20,30,40,50,60,10,80]
# min=l[0]
# for i in range(len(l)):
#     if l[i]<min:
#         max=l[i]
# print(min)

# a=[1,1,2,2,3,3,4,4]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(a[j],end=" ")

#
# s="iam fulka"
# n=''
# for i in s:
#     n=i+""+n
# p=''
# for j in n.split():
#     p=j+" "+p
# print(p)
#
#
# st="iam fulka"
# l=[]
# for i in st.split():
#     l.append(i[::-1])
# print(' '.join(l))

# l1=[1,2,3,4,5]
# l2=[]
# for i in l1:
#     l2.insert(0,i)
# print(l2)
#
# x=[x for x in reversed(l1)]
# print(x)

# L=len(l1)
# for i in range(int(L/2)):
#     n=l1[i]
#     l1[i]=l1[L-i-1]
# l1[L-i-1]=n
# print(l1)

# n=1234
# print(str(n)[::-1])
# reversed=0
# while n!=0:
#     digit=n%10
#     reversed=reversed*10+digit
#     n//=10
# print(reversed)

# l=[4, 2, 3, -1, -2, 0, 1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l1=[1,1,2,2,3,3,4,5]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]==l1[j]:
#             print(l1[j],end=" ")
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)
#
# res=[]
# [res.append(i) for i in l1 if i not in res]
# print(res)













