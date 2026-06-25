"""
Write a function called second_largest that takes a list of numbers and returns the second-largest unique value in the list.
For example:
second_largest([4, 1, 7, 7, 3])
should return 4 (the largest is 7, the second-largest unique value is 4).
And:
second_largest([10, 5, 10, 8])
should return 8 (largest is 10, second is 8).
"""

# A simple loop pass can handle or potentially we can use set() to remove all duplicate

def second_largest(num_list):
    max = 0
    second_max = 0
    num_set = set(num_list) # Remove all duplicate

    for num in num_set:
        if num > max:
            second_max = max
            max = num
        elif num > second_max:
            second_max = num

    return second_max