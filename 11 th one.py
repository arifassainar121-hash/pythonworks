#
# l=1,3,5,7,9
# for i in range(1,10):
#     if(i%2!=0):
#         print(i)

# l=1,3,5,7,9
# for i in l:
#     print(i)
#
# for i in range(1,10,2):
#     print(i)

# 2,4,6,8,10
#
# for i in range(2,11,2):
#     print(i)

# for i in range(1,11):
#     if(i%2==0):
#         print(i)


# 1,4,9,16,25
#
# for i in range(1,6):
#     i=i**2
#     print(i)


#
# 4,9,14,19,24,29,34,39
# for i in range(4,40,5):
#     print(i)
#
# 5,4,3,2,1

# for i in range(5,0,-1):
#     print(i)
# 8,6,4,2,0
# for i in range(8,-1,-1):
#     if(i%2==0):
#         print(i)
#


# i=8
# while(i>=0):
#     print(i)
#     i=i-2

# for i in range(8,-1,-2):
#     print(i)

# 7,14,21,28,35,42
# for i in range(7,43,7):
#     print(i)


# 100,200,300...1000
# 1,8,27,64,125
#
# find all 3 digit number are divisible by 3
# color =['red','green','blue','yellow','black']
# print reverase of each color




# for i in range(100,1001,100):
#     print(i)
#
#
# for i in range(1,6):
#     i=i*3
#     print(i)
#
#
# for i in range(100,1000):
#     if(i%3==0):
#         print(i)


# color=['red','green','blue','yellow','black']
# for i in range color:
#     print(color[::-1])



# n=1,2,3,4
# for i in str(n):#   "1,2,3,4"
#     print(i)
#
#
# sum of digit of  numbers 1+2+3+4=>10
# n=1234
# sum=0
# for i in str(n) :
#     sum=sum+int(i)
#     print(sum)



# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)


# l=[1,2,3,4]
# new=str()
# for i in l:
#     new.add(i**2)
#
# print(new)
#
#
# give a string
#
# s='hello world'
# new=''
# vowel='aeiou'
# for i in s:
#     if i in vowel:
#         new=new+i
# print(new)
#
# create
# a
# new
# dictionasry
# wheere
# kwy
# are
# numbers
# n
# d
# values
# are
# sque of each number
#
# # new-{1:1,2:4,3:9,4;16}
# dictionary=value

# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
#
# print(new)
# h='hello'
# new=''
# for i in h:
#     new=i+new
# print(new)('')

# s=1,2,3,4
# new=""
# for i in str(s):
#     new=i+new
#     print(new)

#
# create
# a
# new
# dictionasry
# wheere
# kwy
# are
# numbers
# n
# d
# values
# are
# sque
# of
# each
# numbe





# s='hello'
# for i in s:
#     if(i=='l'):
#         break
#     print(i)

#
# s='hello'
# for i in s:
#     if(i=='l'):
#         continue
#b       print(i)



# l=[25,67,34,78,17,44,82]
# print all numbers
# stop the lopp when i>50
# skip all even numbers

# l=[25,67,34,78,17,44,82]
# for i in l:
#     print(i)

# l=[25,67,34,78,17,44,82]
# for i in l:
#     if(i>50):
#         break
#     print(i)



# l=[25,67,34,78,17,44,82]
# for i in l:
#     if(i%2!=0):
#         print(i)

# l=[25,67,34,78,17,44,82]
# for i in l:
#     if(i%2==0):
#         continue
#     print(i)

    # 1.
    # Given
    # a
    # list
    # of
    # numbers
    #
    # l = [25, 67, 34, 78, 17, 44, 82]
    #
    # # print all numbers
    # # stops the loop when i >50
    #
    # # skips all even numbers
    #
    # 2.
    # Given
    # a
    # list
    # 1.Given a list of numbers
#
# l=[25,67,34,78,17,44,82]
#
# #print all numbers
# #stops the loop when i >50
#
# #skips all even numbers
#
# 2.
# Given a list colors=['red','green','yellow','blue','orange','black']
# #print all colors
# #print those colors starting with 'b' #blue black
# #print the first color starting with 'b' #blue
#
# #skips all colors starting with 'b'
    # # print all colors
    # # print those colors starting with 'b' #blue black
    # # print the first color starting with 'b' #blue
    #
    # # skips all colors starting with 'b'

# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     print(i)


# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     if i[0]=='b':
#         print(i)

# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
    # if i[0]=='b':
    #     print(i)
    #     break

# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     if i[0]!='b':
#         print(i)

colors=['red','green','yellow','blue','orange','black']
for i in colors:
    if i[0]=='b':
        continue
    print(i)


# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5

# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]




# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25



# 4.Given a list, sum only the elements at even indices.
l=[10,20,30,40,50]
# Example:
#  → Sum = 10 + 30 + 50 = 90



#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
l=[4,9,1,0,6,7]


# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.


# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.




# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"





#
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
l=[5,2,8,6,2]


# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"

digits="0123456789"



# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]

# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"



# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
#
#
# 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students

# for i in d.values:
#     print(i[0])

#
# 16.Write a program to print the numbers from 1 to 100.
# But for multiples of:
#
# 3, print “Fizz” instead of the number
#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# Otherwise, print the number itself
#
# Output format example:
# 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …
#
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break
#
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number
#
