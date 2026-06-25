"""
Write a function called merge_dicts that takes two dictionaries where the values are numbers, and returns a single dictionary that combines them — if a key appears in both, its values should be added together.
For example:
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
should return:
{"a": 1, "b": 5, "c": 4}
("b" appears in both, so 2 + 3 = 5; "a" and "c" appear in only one each, so they carry over unchanged.)
"""

# Create two seperated set to get all the items within each set.
def merge_dicts(dict_a, dict_b):
    set_A = set(dict_a) # all the key in dict a
    set_B = set(dict_b) # all the key in dict b
    merged_set = set_A | set_B

    output_dict = {}
    for key in merged_set:
        if key not in output_dict:
            output_dict[key] = 0

        if key in dict_a:
            output_dict[key] += dict_a[key]
        if key in dict_b:
            output_dict[key] += dict_b[key]

    return output_dict
            
