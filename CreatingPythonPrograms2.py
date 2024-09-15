###
# Project:      CreatingPythonPrograms2.py
# Author:       Michael Keeton
# Created:      09/15/2024
# Description:  Find the multiplication and division of two numbers.
###

def main():
    # Ask user to input two numbers.
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    
    # Multiply the two numbers and output the result.
    print(num1, '*', num2, '=', num1 * num2)
    
    # Divide the two numbers and output the result.
    print(num1, '/', num2, '=', num1 / num2)

main()