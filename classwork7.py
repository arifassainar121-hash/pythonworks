import functools

# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# result=list(map(lambda name : name.capitalize(),names))
# print(result)

#
# 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# new=list(map(lambda user:user +'@gmail.com',users))
# print(new)
# 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# new=list(filter(lambda word : word.strip(),words))
# print(new)
# words = ['hello', ' ', 'world', ' ', 'python']
# new="".join(words)
# print(new)

# words = ['hello', ' ', 'world', ' ', 'python']
# new=list(filter(lambda word : ''.join(word),words))
# print(new)

# words = ['hello', ' ', 'world', ' ', 'python']
# new=list(filter(lambda word : word!="",words))
# print(new)

# 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# new=list(filter(lambda name: name.upper[0],names))
# print(new)

# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# new=list(filter(lambda name: name[0]=='A',names))
# print(new)
#
# 5.Concatenate all strings in a list
# words = ['Python', 'is', 'fun']
# from functools import reduce
# words = ['Python', 'is', 'fun']
# result=reduce(lambda x, y: x + ' ' + y, words)
# print(result)

# 6.Multiply all numbers in a list
# nums = [2, 3, 4]
# new=list(map(lambda num:num*2,nums))
# print(new)

# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
# print(list(map(lambda word:word[0],words)))


# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,words)))
# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
    # a=list(filter(lambda x:x>0,l))
    # #Sum of Positive Odd numbers
    # a=list(filter(lambda x:x<0 and x%2==0,l))
    # #Sum of Negative  odd numbers
    # a=list(filter(lambda x:x<0,l))
    # #Sum of Negatve Even numbers
# a=list(filter(lambda x:x<0,l))
    # #Count of Positive numbers
# a=list(filter(lambda x:x<0,l))
    # #Count of negative numbers
# a=list(filter(lambda x:x<0,l))
#print(a)
# 10.Given a list nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]


# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
l=list(map(lambda x:x.get('name').upper(),p))
print(l)

#print products with price greater than 10000
l=list(map(lambda x:x['price']>1000,p))
print(l)

#Find the total price of all products
print(functools.reduce(lambda x,y:x+y['price'],p,0))