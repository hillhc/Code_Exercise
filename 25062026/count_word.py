'''
Write a function called count_words that takes a sentence (a string) and returns a dictionary where each key is a word and each value is how many times that word appears.
For example:
count_words("the cat sat on the mat")
should return:
{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}

Very Easy
'''

### Simpliest approaches, utilize regular expression to phrase the string, then store a dictionary to count the occurance of each words.

import re

def count_words(input_string):
    phrased_word = re.findall(r'[A-Za-z]+',input_string) # Return all consecutive chara list
    word_counts = {} # Empty dict
    for word in phrased_word:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts