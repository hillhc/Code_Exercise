'''
Write a function called longest_unique_substring that takes a string and returns the length of the longest substring that contains no repeating characters.
For example:
longest_unique_substring("abcabcbb")   → 3    ("abc" is the longest, length 3)
longest_unique_substring("bbbbb")      → 1    ("b", length 1)
longest_unique_substring("pwwkew")     → 3    ("wke", length 3)
longest_unique_substring("")           → 0    (empty string)
'''

def longest_unique_substring(input_string):
    if len(input_string) == 0:
        return 0
    
    substring_dict = {} # For O(1) look up
    max_length = 0
    current_length = 0
    start_point = 0

    for char in input_string:
        if char not in substring_dict:
            substring_dict[char] = 1
            current_length += 1
        else: # Repeated chars
            if current_length > max_length:
                max_length = current_length

            while char in substring_dict:
                substring_dict.pop(input_string[start_point])
                start_point += 1
                current_length -= 1 
            substring_dict[char] = 1
            current_length += 1

    if current_length > max_length:
        max_length = current_length
    
    return max_length