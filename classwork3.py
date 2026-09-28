# #Write a program to check whether two entered numbers are equal or not
#
# n1=int(input("enter the 1st numer: "))
# n2=int(input("enter the 2nd number: "))
# if n1==n2:
#     print("the numbers are equal")
# else:
#     print("the numbers are not equal")


# #Write a program to check whether two entered words are equal or not
# n1=input("enter the 1st word: ")
# n2=input("enter the 2nd word: ")
# if n1==n2:
#     print(n1," is equal to",n2)
# else:
#     print(n1," is not equal to", n2)
# #Write a program to find the maximum of two numbers



# #write a program to check whether the entered character is vowel or not
# s=('a','e','i','o','u')
# n=input("enter the character: ")
# if n in s:
#     print("its a vowel")
# else:
#     print("its not vowel")

# #Write a program to check whether the entered country name contains word 'land'
# n=input("enter the country: ")
# if 'land' in n:
#     print("land in country name ")
# else:
#     print("country not in country name ")



# #write a program to check whether the entered number is 3 digit or not

n=int(input("enter the number: "))
if n>=100 and n<=999:
    print("its three digit number")
else:
    print("its not three digit number")




#write a program to check whether the entered string is  palindromde or not
s=int(input("enter the string: "))
if s=s[::-1]:

       print("enter numbers i string")


#Write a program to check whether a number is present in given list
l=[23,67,12,90]
n=int(input("enter the number: "))
if n in l:
    print("present in string")
else:
    print("not present in string")
#Write a program to check whether a key is prsent in a dictionary or not
d={101:'Arun',102:'Amal',103:'Anu'}
key=int(input("enter the number: "))
if key in d.keys():
    print("enterd key is present in the dictionary")
else:
    print("enterd key is not present in the dictionary")

#Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
pass=int(input("enter the password: "))
if len(pass/>0):
    print("enterd password is strong")
else:
    print("enterd password is weak")
