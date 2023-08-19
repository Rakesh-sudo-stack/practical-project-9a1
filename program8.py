# Voting Eligibility Check
# Q. WAP to check if a person is eligible for voting or not:- 

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

"""
Sample Outputs:-
1. (Case = 18):
    You are eligible to vote
2. (Case = 57):
    You are eligible to vote
3. (Case = 12):
    You are not eligible to vote
"""