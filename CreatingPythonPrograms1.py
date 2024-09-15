###
# Project:      CreatingPythonPrograms1.py
# Author:       Michael Keeton
# Created:      09/15/2024
# Description:  Find the addition and subtraction of two numbers.
###

def main():
    # Ask user to input two numbers.
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    
    # Add the two numbers and output the result.
    print(num1, '+', num2, '=', num1 + num2)
    
    # Subtract the two numbers and output the result.
    print(num1, '-', num2, '=', num1 - num2)

main()