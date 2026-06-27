"""
Write a function called remove_duplicates that takes a list and returns a new list with duplicates removed, keeping the original order of first appearance.
For example:
remove_duplicates([3, 1, 3, 2, 1, 5])   → [3, 1, 2, 5]
remove_duplicates(["a", "b", "a", "c"])  → ["a", "b", "c"]
"""

def remove_duplicates(input_list):
    seen = set()
    output_list = []
    
    for element in input_list:
        if element not in seen:
            seen.add(element)
            output_list.append(element)

    return output_list