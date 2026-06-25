"""
Write a function called group_anagrams that takes a list of strings and groups together the ones that are anagrams of each other (same letters, rearranged). Return a list of lists, where each inner list contains words that are anagrams.
For example:
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
should return (order of groups doesn't matter):
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(input_list):
    output_groups = []
    words_dict = {}


    
    for word in input_list:
        sorted_word = str(sorted(word.lower())) # A list of char, the aggregate them --> Suggestion from AI marker: "".join(sorted(word.lower())) would be better
        if sorted_word not in words_dict:
            words_dict[sorted_word] = [word]
        else:
            words_dict[sorted_word].append(word) 
    
    for _, values in words_dict.items():
        output_groups.append(values)
    
    return output_groups