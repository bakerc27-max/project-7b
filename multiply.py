# Author: Chloe Baker
# GitHub username: bakerc27_max
# Date: 05/13/2026
# Description: Calculates the product of two positive integers using addition

def multiply(num1, num2):
    """Return the product of two positive integers using addition."""
    
    if num2 == 1:
        return num1
    else: 
        return num1 + multiply(num1, num2 - 1)
