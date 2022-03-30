# from abc import ABC,abstractmethod
# class srikanthdemo(ABC):
#     @abstractmethod
#     def display(self):
#         None
#     @abstractmethod
#     def show(self):
#         None
# class demo(srikanthdemo):
#     def show(self):
#         print("ABSTRACT METHOD")
# class demo1(srikanthdemo):
#     def show(self):
#         print("SHOW METHOD")
#     def display(self):
#         print("DISPLAY METHOD")
# obj=demo1()
# obj.show()
# obj.display()

# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         c=a
#         a=b
#         b=c+b
# fib(5)


# from threading import *
# from time import sleep
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("HELLO")
#             sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
#
# t1=Hello()
# t2=Hi()
# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("BYE")

# s='siva'
# n=""
# for i in s:
#     n=i+n
# print(n)
# print(s[::-1])




