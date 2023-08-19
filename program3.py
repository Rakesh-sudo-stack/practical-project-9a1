#Four Functions Calc
#Q. WAP to make a four functions basic calculator:- 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation(+,-,*,/): ")
if op == "+":
    print(num1,"+",num2,"=",num1+num2)
elif op == "-":
    print(num1,"-",num2,"=",num1-num2)
elif op == "*":
    print(num1,"*",num2,"=",num1*num2)
elif op == "/":
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid operation")

"""
Sample Outputs:- 
1. [Case = (4,5,+)]:
    4 + 5 = 9
2. [Case = (9,3,*)]:
    9 * 3 = 27
"""