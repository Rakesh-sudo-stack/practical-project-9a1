# Print first 10 prime num
# Q. WAP to find first 10 prime numbers:- 

count = 0
num = 2
while count < 10:
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        print(num, end = " ")
        count += 1
    num += 1

"""
OUTPUT:-
2 3 5 7 11 13 17 19 23 29
"""