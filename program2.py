#Prime Num Check
#Q. WAP to find if a number is prime or not

n = int(input("Enter any no: "))

if n<=1:
    print("It is not a prime number")
elif n == 2:
    print("It is a prime number")
else:
    for i in range(2,n):
        if not n % i:
            print("It is not a prime number")
            break
        if i == n - 1:
            print("It is a prime number")

"""
Sample Outputs:-
1. (Case = 5):
    It is a prime number
2. (Case = 9):
    It is not a prime number
"""