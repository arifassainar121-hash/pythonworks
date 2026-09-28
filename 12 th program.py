#check a number is armstrong number
# l="153"
# sum=0
# for i in l:
#     sum=sum+int(i**3)
#     print(sum)
#
# l=int(input("enter  number: "))
# m=str(l)
# sum=0
# n=len(m)
# for i in m:
#     sum=sum+int(i)**n
# print(sum,end="")

# num=int(input("ennter  number: "))
# s=str(num)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if sum==num:
#     print("yes")
# else:
#     print("no")

# factorbof numbers
#
# n=int(input('enter number: '))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=' ')

# pass(nuull statement)
#
# for i  in range(1,11):
#     pass
# print(i)


# for else

# for i in range(1,6):
#     print(i,end=' ')
# else:
#     print('hi')

# for i in range(1,6):
#     if(i%3==0):
#         break
#     print(i)
# else:
#     print("hello")

#
# n=int(input("enter number: "))
# if(n>1):
#
#     for i in range(2,n):
#         if(n%2==0):
#             print(n,'is not prime')
#             break
#     else:
#          print(n,'is prime')
# else:
#     print('not prime and prime')


# nested loop


# l=[10,20,30]
# for i in l:
#     for j in range(1,4):
#         print(i,end=' ')
#     print(i)



# l=[1,2,3]
# for i in l:
#
#     for j in range(1,5):
#         print(i,end=' ')
#     print(i)



# l=[1,2,3]
# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()

#
# l=[1,2,3]
# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end=" ")
#     print()

# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
    # print(i)
    # for j in i:
    #     print(j)



# names=['kelly','alan','jeny']
# print
#
# kelly  kelly kelly
# alan alan alan
# jeny
# jeny jeny

# l=['kelly','alan','jeny']
# for i in l:
#     # print(i)
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


# for i in l:
#     print(i)
#     for j in i:
#         print(i,end=" ")
#     print()

# n=[1,2,3]
#
# q=['what','when','why']
#
# print
#
# what when why
# what when why
# what when why
#
# q=['what','when','why']
# for i in q:
#     print(i)
#     for j in range(1,4):
#         print(q,end=" ")
#     print()


#
# d=[
# {'id':101,'name':'arun','age':23},
# {'id':102,'name':'alan','age':24},
# {'id':103,'name':'anu','age':25}]

# for i in d:
#     print(i)
#     for j in i.values():
#         print(j)
#     print()

# for i in d:
#     for k,j in i.items():
#         print(k,j)
#     print()

# *
# **
# ***
# ****


# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# *
# ***
# *****
# ******
#
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


# 1
# 22
# 333
# 4444


# for i in range(1,5):
#     # print(i)
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

#
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()



#
# 1
# 12
# 123
# 1234


# l=[23,45,78,90,12,13,91]
# # print all prime number
#
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             # print('not prime')
#             break
#         print('i')


    # prime range(1,100)
#
# for i in range(2,100):

#     for j in range(2,i):
#         if(j%2==0):
#             print(i,"not")
#             break
#         else:
#              print(i,"prime")


# n=int(input("enter number: "))
# if(n>1):
#
    # for i in range(2,n):
    #         if(n%2==0):
    #             print(n,'is not prime')
    #             break
    #     else:
    #          print(n,'is prime')
    # else:
    #     print('not prime and prime')
    # armstrong number range (100,1000)



    #
    #
# n=[]
# for i in range(100,1000):
#     l=str(i)
#     m=len(l)
#     sum=0
#     sum=sum+int(m)**3
#
#     if sum==m:
#         n.append(i)
# print(n)

# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
#
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
#     1
#     23
#     456
#     78910

# k=1
# for i in range(1,5):
#     for j in range(1,1+i):
#         print(k,end=' ')
#         k=k+1
#     print()
#
#
# a
# b c
# d e f
# g h i j

# k=ord('a')
# for i in range(1,5):
#     for j in range(1,1+i):
#         print(chr(k),end=' ')
#         k=k+1
#     print()

# a
# bb
# c c c
# d d d d



# k = ord('a')
#
#
# for i in range(1, 5):
#     for j in range(1, 1 + i):
#         print(chr(k), end=' ')
#     k = k + 1
#     print()

# a
# a b
# a b c
# a b c d

#
# for i in range(1, 5):
#     k = ord('a')
#     for j in range(1, 1 + i):
#         print(chr(k), end=' ')
#         k = k + 1
#     print()
#
#
# 1000
# 0200
# 0030
# 0004

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 1
# 1 0
# 1 0 1
# 1 0 1 0
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4


# for i in range(1,5):
#     k=1
#     for jn in range(1,i+1):
#         print(k,end=' ')
#         k+=1
#     print()

# a
# a b
# a b c
# a b c d


# for i in range(1,5):
#     k=ord('a')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()


 #    *
 #   **
 #  ***
 # ****

# k=3*2
# # for i in range(1,5):
# #     for p in range(1,k+1):
# #         print(end=" ")
# #     for j in range(1,i+1):
# #         print('*',end=' ')
# #     k=k-1
# #     print()

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#
#     for j in range(1,i+1):
#         print('*',end='')
#     k=k-1
#     print()
#
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#
#     for j in range(1,i+1):
#         print('*',end='  ')
#     k=k+1
#     print()

# s=3*2
# k=2
# for g in range(1,5):
#     for s in range(s,s+1):
#         print(" ",end=' ')
#     for b in range(1,g+1):
#         print('*',end='  ')
#     g=g-1
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#
#     for j in range(1,i+1):
#         print('*',end='  ')
#     k=k+1
#     print()
#
# l=[1,2,3,4]
# new=[i**2 for i in l]
# print(new)

# new=[i**3 for i in l]
# print(new)
# new=[5 for i in l]
# print(new)

# l=[23,46,42,48,68,98]
#
# new=[i for i in l if i%2==0]
#
# new=[i for i in l if i>50]
# print(new)


#Given a list
# l=[12,45,34,67,90]
# # create a new list with even values
#
# new=[i for i in l if i%2==0]
# print(new)
#
#
# #create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)

#Given  a list
# colors=['red','green','blue','orange']
# # create a new list with first letter of each color
# # new=[i[0] for i in colors]
# # print(new)
# # create a new list with length of each color
# new=[len(i) for i in colors]
# print(new)




    # # create a new list of cubes
# l = [1, 2, 3, 4]
    #

# new=[i**3 for i in l]
# print(new)
    # # create a new list of square roots
    # l = [25, 36, 81, 100]
# new=[i**2 for i in l]
# print(new)
    #
    # # create a new list of lengths
    # colors = ['red', 'green', 'blue', 'yellow', 'black']
    # # create a new list of first characters
    # # create a new list of last characters
    # # create a new list of reverse of each elemnt
    #
    # # Given a list l=[23,78,12,56]
    # # Add 10 to each element in the given sequence
    #
    # ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#     # #
#     # # # create a new list of emails
# new=[i'email' for i in l]
# print(new)


# # #create a new list with square root of each element
# # l=[25,16,9,36]


# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
# # create a list of marks
#
# #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
# #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
# #create a list of positive numbers
# new=[i for i in l if type(i)==str and i>0]
# print(new)

#
#
# #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
# new=[ i for i in fruits if len(i)>6 ]
# print(new)
# #create a new list with elements whose value is divisible by 3 in range(1,101)
new=[i for i in range(1,101) if i%3==0]
print=(new)
# Given s="python coding  is easy and fun"
# # create a new list with only vowels


new=[ i for i in  ]

