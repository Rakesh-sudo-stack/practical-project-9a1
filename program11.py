# Palindrome Check
# WAP to check if a string is a palindrome:- 

string = input("Enter a string: ")

if string == string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

"""
Sample Outputs:- 
1. (Case = "Rakesh"):
    It is not a palindrome
2. (Case = "KANAK"):
    It is a palindrome
3. (Case = "NAWAL"):
    It is not a palindrome
"""