#Buzz Number
#Q. WAP to find a buzz number:-

num = int(input("Enter any no: "))
if num % 7 == 0 or num % 10 == 7:
    print(num,"is a buzz number")
else:
    print(num,"is not a buzz number")

"""
Sample Outputs:-
1. (Case = 14) - 
    14 is a buzz number
2. (Case = 87) - 
    87 is a buzz number
3. (Case = 15) - 
    15 is not a buzz number
"""