"""
Write a function called is_palindrome that takes a string and returns True if it reads the same forwards and backwards, ignoring spaces and capitalisation, and False otherwise.
For example:
is_palindrome("racecar")        → True
is_palindrome("Race car")       → True   (ignore spaces and capitals)
is_palindrome("hello")          → False
"""

# Find the centre of the string, (remove all spaces (or just ignore) and convert capitals). Then iterate from the centre
def is_palindrome(input_string):
    input_string = input_string.lower().replace(" ","")
    string_length = len(input_string)
    if string_length <= 1:
        return False
    elif string_length % 2 == 1: # Odd length directly start at centre
        left = (string_length + 1)//2 - 2 # Pointer to left
        right = (string_length + 1)//2    # Pointer to right
        is_palindrome_flag = True
        while left >= 0 and right < input_string.len():
            if input_string[left] != input_string[right]:
                is_palindrome_flag = False
                break
            left -= 1
            right += 1
        return is_palindrome_flag
    else: ## Even case
        left = (string_length //2) - 1
        right = (string_length //2)

        is_palindrome_flag = True
        while left >= 0 and right < input_string.len():
            if input_string[left] != input_string[right]:
                is_palindrome_flag = False
                break
            left -= 1
            right += 1
        return is_palindrome_flag
    
    return False