# Factorial
# Q. WAP to find factorial of a number:- 

num = int(input("Enter a number: "))
f = 1
for i in range(1, num+1):
    f *= i
print("Factorial =",f)

"""
Sample Outputs:- 
1. (Case = 4): 
    Factorial = 24
2. (Case = 5): 
    Factorial = 120
"""