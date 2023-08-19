# Reversing a Number
#WAP to reverse the digits of a number:- 

num = int(input("Enter a number: "))

dig = 0
while num > 0:
    r = num % 10
    dig = dig * 10 + r
    num //= 10

print(dig)

"""
Sample Outputs:- 
1. (Case = 1243):
    3421
2. (Case = 12112145)
    54121121
"""