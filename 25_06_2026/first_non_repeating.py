'''
Write a function called first_non_repeating that takes a string and returns the first character that appears exactly once. If every character repeats (or the string is empty), return None.
For example:
first_non_repeating("leetcode")    → "l"   ('l' is the first char that appears only once)
first_non_repeating("aabbcc")      → None  (every character repeats)
first_non_repeating("aabbcdd")     → "c"   ('a' and 'b' repeat, 'c' appears once)
'''
def first_non_repeating (input_string):
    input_string = input_string.replace(" ","").lower()
    char_dict = {} # For recording the occurance of character

    for i, charcter in enumerate(input_string):
        if charcter not in char_dict:
            char_dict[charcter] = [1, i] # Count of occurance and char position in input string
        else:
            char_dict[charcter][0] += 1
    
    output_char = None
    char_pos = 0
    for key, values in char_dict.items(): 
        if values[0] > 1:
            continue
        else:
            if output_char == None:
                output_char = key
                char_pos = values[1]
            elif values[1] < char_pos:
                output_char = key
                char_pos = values[1]
    
    return output_char