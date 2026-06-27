"""
Write a function called group_by_length that takes a list of words and returns a dictionary where each key is a word length, and each value is a list of the words that have that length.
For example:
group_by_length(["cat", "dog", "fish", "a", "bird"])
should return:
{3: ["cat", "dog"], 4: ["fish", "bird"], 1: ["a"]}
"""

def group_by_length(input_list):
    output_dict = {}
    words_set = set(input_list) # in case of duplicated words

    for word in words_set:
        word_length = len(word)

        if word_length not in output_dict:
            output_dict[word_length] = [word]
        else:
            output_dict[word_length].append(word)
    
    return output_dict
        