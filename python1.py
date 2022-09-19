# l=[]
# for i in range(2000 ,3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# #print(l,end=",")
# #program2
# str=("rajeghegsjh")
# #print(len(str))
# #
# str="12344"
# print(int(str))
# #print(float(str))
# #
# l=[1,2,4,5,6,7,8,9]
# print(l)
# #print(tuple(l))
# t=(1,2,3,4,5,66,7,8,9)
# print(t)
# #print(list(t))
# dict={"name":"raji","age":"24","year":"1997"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# #
# l=[11,32,43,44,55,66,76]
# print(l)
# l[2]=95
# print(l)
# t=(11,23,44,55,66,77)
# print(t)
# #
# #
# d='welcome to python'
# print(d)
# x=(d[4:10])
# print(x)
#
# t=(1,"one"),(2,"two"),(3,"three")
# print(t)
# a=dict(t)
# print(a)
#
# str='welcome to python'
# a=str[::-1]
# print(a)
# str='welcome to python'
# a=str[::-2]
# print(a)
# a=str[::-3]
# print(a)
#
# l=[10,5,4,20,1,15,12]
# l.sort()
# print(l)
# #
# l=["one","two","three"]
# s=[1,2,3]
# mydict=dict(zip(l,s))
# print(mydict)
#
# list = [22, 44, 66, 56, 77, 89]
# l=[]
# for i in list:
#     #if i%2 ==0:
#         l.append(i)
# print(l)

# l=[]
# for i in range(2000 ,3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# #print(l,end=",")
# #
# str=("rajeghegsjh")
# #print(len(str))
# #
# str="12344"
# print(int(str))
# #print(float(str))
# #
# l=[1,2,4,5,6,7,8,9]
# print(l)
# #print(tuple(l))
# t=(1,2,3,4,5,66,7,8,9)
# print(t)
# #print(list(t))
# dict={"name":"raji","age":"24","year":"1997"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# #
# l=[11,32,43,44,55,66,76]
# print(l)
# l[2]=95
# print(l)
# t=(11,23,44,55,66,77)
# print(t)
# #
# #
# d='welcome to python'
# print(d)
# x=(d[4:10])
# print(x)
#
# t=(1,"one"),(2,"two"),(3,"three")
# print(t)
# a=dict(t)
# print(a)
#
# str='welcome to python'
# a=str[::-1]
# print(a)
# str='welcome to python'
# a=str[::-2]
# print(a)
# a=str[::-3]
# print(a)
#
# l=[10,5,4,20,1,15,12]
# l.sort()
# print(l)
#
# l=["one","two","three"]
# s=[1,2,3]
# mydict=dict(zip(l,s))
# print(mydict)
#
# list = [22, 44, 66, 56, 77, 89]
# l=[]
# for i in list:
#     #if i%2 ==0:
#         l.append(i)
# print(l)
# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]
# print(dict(zip(l1, l2)))
#17 program
# def merge(dict1,dict2,dict3):
#     result=dict1|dict2|dict3
#     return result
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4=merge(dict1,dict2,dict3)
# print(dict4)
#19 program
#
# l=[10,20,30,40,50,50,40,30,20,10]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#20 program
# s={"name":"raji","age":"24","year":"1997"}
# print(dict.values(s))
#18 program
#airthmetic operations
# x=4
# y=5
# print(x+y)
# x=6
# y=4
# print(x-y)
# x=3
# y=70
# print(x*y)
# x=30
# y=3
# print(x/y)
# print(x//y)
# print(x%y)
# x=5
# print(x**2)
#relational
#logical operatoRS
# a=5
# b=4
# if a>0 and b>0:
#     print("a is greater then b")
# else:
#     print("a is less then b")
# a=9
# b=4
# if a>b:
#     print("a is greater then b")
# else:
#     print("a is less then b")
# a=6
# b=9
# if a>0 or b>5:
#     print("a is greater then 0")
# else:
#     print("b is greater then 5")
#not operator
# x=5
# y=9
# if not x>y:
#     print("raji")
# else:
#     print("rajeswari")
#not
# a=4
# b=4
# if not a>b:
#     print("a is greater")
# else:
#     print("a is lesser")
# from array import *
#
# array1 = array('i', [10,20,30,40,50])
#
# print (array1.index (50)+1)


# s="dfgegdcv tej raj baj".split()
# k = s[::-1]
# for i in k:
#     print(i)
# #print(k)
#1 program number of ocurrences in dict
# s=input("enter number")
# d={1:['a','G','k','l'],2:['G','b','c'],3:['a','k','G','c']}
# count=0
# for i in d:
#     count=count+1
# print(count)
#2 program specified list removing given list
# l=['red','green','white','black','pink','yellow']
# l1=(l.pop())
# print(l1)
# l2=(l.pop(0))
# print(l2)
# l3=(l.pop(3))
# print(l3)
# print(l)
#3 program count the number of the strings from the given string len is 1&last char the same from given list of str
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


