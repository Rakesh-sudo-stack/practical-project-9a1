# Find greatest num among 3
# Q. WAP to find the greatest number among three

a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
c = int(input("Enter num 3: "))
if a > b and a > c:
    print(a,"is the greatest")
elif b > a and b > c:
    print(b,"is the greatest")
elif c > a and c > b:
    print(c,"is the greatest")

"""
Sample Outputs:-
1. [Case = (3, 7, 11)]:
    11 is the greatest
2. [Case = (19, 57, 6)]:
    57 is the greatest
"""