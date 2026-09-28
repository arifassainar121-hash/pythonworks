# l={2,4,6,3,7}
# new={i:i**2 for i in l}
# print(new)


# l=[10,20,30,40]
# output[0:10,2:20,2:30,3:40]
# new={i:l[i] for i in range(0,4)}
# print(new)
#
# new={i:l[i] for i in range(len(l))}
# print(new)

# s='hello world'
# for i in s.split():
#     print(s)


# keys are words and values are length

# s= "python code is easy and fun"
# new={i:len(i) for i in s.split()}
# print(new)


def  add():
    #adding 2 numbers
    n1=int(input("enter the first number"))
    n2=int(input("enter the second number"))
    sum=n1+n2
    print("the sum is",sum)

    retrun

add()
