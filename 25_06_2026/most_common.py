"""
Write a function called most_common that takes a list of items and returns the item that appears most frequently.
For example:
most_common(["apple", "banana", "apple", "cherry", "apple"])   → "apple"
most_common([1, 2, 2, 3, 2, 1])                                 → 2
"""

def most_common(input_list):
    common_dict = {}
    for element in input_list:
        if element not in common_dict:
            common_dict[element] = 1
        else:
            common_dict[element] += 1
    
    max_item = None
    max_count = 0
    for item in common_dict:
        if common_dict[item] > max_count:
            max_item = item
            max_count = common_dict[item]
    
    return max_item