#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
#
#
# n=int(input("enter BMI(Body Mass INdex): "))
# if n<=18.4:
#     print("underweight")
#     if n<=18.4 and n>=24.9:
#         print("normal")
#     else:
#         print("overweight")
# else:
#     if n>=40:
#         print("obese")
#     else:
#         [print("invalid")]





    #2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.



#
# product_code=int(input("enter product code: 1=Battery BasedToys,2/key based toys 3/Electrical_Charging_Based_Toys: "))
# amound=int(input("enter amount in RS: "))
# disount=0
# if product_code==1:
#     if amound>1000:
#         disound=amound*0.10
#         payable=amound-disound
#         print("payable amound is",payable)
# elif product_code==2:
#     if amound>100:
#         disound=amound*0.05
#         payable=amound-disound
#         print("payable amound is",payable)
# elif product_code==3:
#     if amound>500:
#         disound=amound*0.10
#         payable=amound-disound
#         print("payable amound is",payable)



#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
#
# n=int(input("enter the  number: "))
# if n%3==0:
#     print("fizz")
#     if n%5==0:
#         print("buzz")
# else:
#     if n%3==0 and n%5==0:
#         print("fizzbuzz")
#     else:
#         print("invalid number")