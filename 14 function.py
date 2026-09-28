# def  add():
#     #adding 2 numbers
#     n1=int(input("enter the first number"))
#     n2=int(input("enter the second number"))
#     sum=n1+n2
#     print("the sum is",sum)
#
#     return
#
# add()
# from dis import JUMP_BACKWARD


# define a funtion disply "hello your name"
# def name():
#     #ask name
#     n=int(input("hello your name: "))
#     print(n)
#
#     return
#
# name()
# define a funtion find the factorial of anumber
# def fact():
#     n=int(input("enter the number"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)
#
#     return
# fact()
# define a funtion find the cound the specific characyer in the g9iveb strig
# def c():
#     n=input("enter the string: ")
#     count=0
#     s=input("enter the character: ")
#     for i in s:
#         if (i==n):
#             count=count+1
#     print(count)
#     return
# c()

# define a funtion check wheter the number is prime or not

# def prime():
#     n=int(input("enter number: "))
#     if(n>1):
#         for i in range(2,n):
#             if(n%i==0):
#                 print("not prime")
#                 break
#             else:
#                 print("prime")
#     else:
#         print("number is not primne and nort prime")
#
#     return
# prime()


# to find the facters of the number

# def f1():
#     # factorial
#     n=int(input('enter the number:     '))
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
#
#     return
# f1()


# sum of two numbers
# def sum(n1,n2):
#     s=n1+n2
#     print("sum",s)
#     return
# sum(15,5)


# def sum(n1,n2):
#     s=n1+n2
#     print("sum",s)
#     return
#
# n1=int(input("enter 1 st number: "))
# n2=int(input("enter 2 st number: "))
# sum(n1,n2)


#
# # difine a funtion that  takes 3 argument amount rate  year as argument\
# #     and  find  simple intrest
# # si=p*n*r/100
# def si(p,n,r):
#     s=p*n*r/100
#     print('simple intrest',s)
#     return
# p=int(input('enter the amount: '))
# n=int(input('enter the year: '))
# r=int(input('enter intrest rate: '))
# si(p,n,r)
#
#
# define a numbers that take two number as argument and return sum as result

#
# def add(n1,n2):
#     s= n1+n2
#     return s
# a=add(n1=5,n2=5)
# print(a)
#
#
# that is a string an argument written a new dictionary wehre the keys are eords and values are length of each word

# l=input("enter the string: ")
# def sting(l):
#     new={}
#     new={i:len(i) for i in l.split()}
#     return new
# a=sting(l)
# print(a)


# define a funtion  tht take number as argument and check whether the number  is spy number or not


#sum of digit =product of digit

#
#   22   2+2=2*2
# 1124

#
# def spy(n,m):
#     s=str(i)
#     sum=0
#     product=1
#
#     for i in n:
#         sum=sum+int(i)
#         product=product+int(i)
#         if(sum==product):
#             print('spy number')
#         else:
#             print('spy number')
#
#
#     return
#
# spy(n)

# def fun(n,a):
#     print('name',n)
#     print('age',a)
#
#
# fun(n='arum',a= 44)


# def fun(*args):
#     print(args)
#
# fun(12,21,'hello',8.09)


# def fun(**kwargs):
#     print(kwargs)
#
# fun(a=10,b=20)


# define a funtion to find the sum opof numbner using  arbitary argument type
#
# def add(*args):
#     pass
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
#
# a=add(10,20)
# b=add(1,2,3,4,5)
# print(a,b)


# import math
# print(math.sqrt(81))

# write a program to  a list of 5 random otp number
# find the position of character in the string
# fefine a function that take the string as argument



#Write a program to create a list of 5 random 3 digit numbers
# #
# import random
# new=[]
# for i  in range(5):
#     num=random.randint(100,999)
#     print(new)
#
# #write a program to create a 5digit random otp number
# n=input('enter a number')


#write a program to find the position of a character in a string

n=int(input('enter the struing: '))
s=str(n)
for i in range(s):
    position=i.find(s)

    print(m)


#define a function that takes a string as argument and returns a new dictionary

#where keys are character and values are count of each character

#Define a function that takes string as argument and print the count of # digits, spaces, letters in that string