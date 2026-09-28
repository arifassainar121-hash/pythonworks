  # looping

# i=1
# while(i<=10):
#     print(i)
#     i=i+1



#while


# # #1,2,3,4,5,.....100
#
# i=1
# while(i<=100):
#     print(i)
#     i=i+1

# # #1,3,5,7,9,11,13,15

# i=1
# while(i<=15):
#     print(i)
#     i=i+2

# #2,4,6,8,10,12
#
# i=2
# while(i<=12):
#     print(i)
#     i=i+2


# #1,4,7,10,13,16

# i=1
# while(i<=16):
#     print(i)
#     i=i+3

#10,20,30,40,50,60,70,80

# i=10
# while(i<=80):
#     print(i)
#     i=i+10

#3,6,9,12,15,18,21

# i=3
# while(i<=21):
#     print(i)
#     i=i+3

#5,4,3,2,1

# i=5
# while(i>=1):
#     print(i)
#     i=i-1

#8,6,4,2,0

# i=8
# while(i>=0):
#     print(i)
#     i=i-2

#100,101,102,.....200

# i=100
# while(i<=200):
#     print(i)
#     i=i+1


#print all 4 digit numbers(1000-9999)

#
# i=1000
# while(i<=9999):
#     print(i,end=" ")
#     i=i+1

# #1,4,7,10,13,16
# i=1
# while(i<=5):
#     print(i**2, end=" ")
#     i=i+1


# print those number  are divisible 3 in range(1,50)

# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i)
#     i=i+1

# print those three digit numbers that are divisible by 5 and 7
#
# i=100
# while(i<=999):
#     if(i%5==0 and i%7==0):
#         print(i)
#     i=i+1


#print those numbers in the  range(100,200) which contain digit '3'
#
# i=100
# while(i<=200):
#     s=str(i)
#     if('3' in s):
#         print(i)
#        i=i+1

    # print those number  are divisible 3 in range(1,50) print count

#
# i=1
# count=0
# while(i<=50):
#       if(i%3==0):
#           ##print(i)
#           count=count+1
#       i=i+1
# print(count)


#print those numbers in the  range(100,200) which contain digit '3'

# i=100
# count=0
# while(i<=200):
#      s=str(i)
#      if('3' in s):
#          #print(i)
#             count=count+1
#      i=i+1
# print(count)


# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)

#sum of first 10 even numbers

#
# i=2
# sum=0
# while(i<=20):
#     if(i%2==0):
#         sum=sum+i
#         print(i)
#     i=i+1
# print("sum" ,sum)


#prodct of first 10 even numbers

#
# i=2
# sum=0
# while(i<=10):
#     if(i%2==0):
#         sum=sum+i
#         print(i)
#     i=i+1
# print("sum" ,sum)

# #4,9,14,19,24,,29,34,39
# sum of the series 1,3,5,7,9,11
#   product of the number  that are divisible by 3 and 5 in range (1,50)
#   cound 3 digit number that are divis9ible by 7


# 1
#
# i=4
# while(i<=40):
#
#     print(i)
#     i=i+5


    #2)
#
# i=1
# sum=0
# while i<=11:
#     print(i)
#     i=i+2
#     sum=sum+i
# print(sum)
 #3
#  i=1
#  sum=1
#  while(i<=50):
#       if(i%3==0 and i%5==0):
#           sum=sum*i
#           print(i,sum)
#       i=i+1
#
# print("product: ",sum)



#
#             #4
#
# i=1
# count=0
# while i>100 and i<999:
#     if(i%7==0):
#         count=count+1
#         i=i+1
#         print(count)
#
#
#
#         factorial of a numberr
#
#         multiplication table of a  number  uo to10

# i=1
# n=int(input("Enter a number: "))
# f=1
# while(i<=n):
#       f=f*i
#       i=i+1
#       print("factorial",f)
#


#
# n=int(input("Enter a number: "))
# i=1
# while(i<=10):
#       print(n,'*',i,'=',n*i)
#       i=i+1

#
# s='hello'
# for i in s:
#     print(i)
#
# l=['red','green','blue']
# for i in l:
#     print(i)
#
# s={1,2,3,4}
# for i in s:
#     print(i)
#
# d={'a':10,'b':20,'c':30}
# for i in d:
#       print(i)
#
# for i in d.values():
#     print(i)




# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)

# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if(i%2==0):
#         print(i)
#
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if(i%5==0):
#         print(i)
#
# l = [12, 34, 56, 45, 89, 16, 69, 33]
# for i in l:
#     if('3' in str(i)):
#         print(i,end=' ')



#
# give a dictionary
#   d={'n1':23,'n2':46,'n3':89,'n4'=24}
#   print  each velues
#   print odd values

# d={'n1':23,'n2':46,'n3':89,'n4':24}
# for i in d.values():
#     print(i)
#
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# for i in d:
#     if i%2!=0:
#         print(i)


#   give a list l=['red','green', 'orange','blue','black','yellow']
#   print each color
#   priint color start with 'b'
# print colour those lenmgth is greather 5


# l=['red','green', 'orange','blue','black','yellow']
# for i in l:
#     print(i)
#
# l=['red','green', 'orange','blue','black','yellow']
# for i in l:
#     if i[0]=='b':
#     print(i)
#
# l=['red','green', 'orange','blue','black','yellow']
# for i in l:
#       if len(i)>5:
#       print(i)
#
#   Given
#   a
#   list
#   l = [10, 'arun', 'amal', 35, 3.6, 6.9, 89]
#   print
#   string
#   values
#   print
#   float
#   values

# l=[10, 'arun', 'amal', 35, 3.6, 6.9, 89]
# for i in l:
#       if type(i)==str:
#           print(i)
#
# l=[10, 'arun', 'amal', 35, 3.6, 6.9, 89]
# for i in l:
#     if type(i)==float:
#         print(i)

# i=[45,78,90,12,67]
#
#  sum of list
# product of list
#   product of even value
#   count of odd value

# sum=0
# l=[45,78,90,12,67]
# for i in l:
#     sum=sum+i
#     print(sum)
#
#
# sum=0
# i=[45,78,90,12,67]
# for i in l:
#     if(i%2==0):
#         sum=sum+i
#         print(sum)

#
# i=1
# # l=1,3,5,7,9
# for i in range(1,9):
#     print(i+2)
# 2,4,6,8,10
# 1,4,9,16,25
#
# 4,9,14,19,24,29,34,39
#
# 5,4,3,2,1
# 8,6,4,2,0
#
# 7,14,21,28,35,42

