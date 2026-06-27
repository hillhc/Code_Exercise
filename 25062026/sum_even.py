"""
Write a function called sum_even that takes a list of numbers and returns the sum of only the even numbers in it.
For example:
sum_even([1, 2, 3, 4, 5, 6])   → 12     (2 + 4 + 6)
sum_even([1, 3, 5])            → 0      (no evens)
"""

def sum_even(input_list):
    even_sum = 0
    for element in input_list:
        if element % 2 == 0:
            even_sum += element
    return even_sum