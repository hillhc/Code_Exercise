'''
Write a function called two_sum that takes a list of numbers and a target number, and returns the indices of the two numbers that add up to the target.
For example:
two_sum([2, 7, 11, 15], 9)    → [0, 1]    (because 2 + 7 = 9, at indices 0 and 1)
two_sum([3, 2, 4], 6)         → [1, 2]    (because 2 + 4 = 6, at indices 1 and 2)
You can assume there's exactly one valid answer. (Two sum solutions always exist)
'''

def two_sum(num_list, target_sum):
    sum_dict = {} # Storing the difference between each indices with the two_sum target
    for i, num in enumerate(num_list):
        if num in sum_dict:
            return [sum_dict[num][1],i]
        
        # run the add afterwards, to avoid counting itself
        num_diff = target_sum - num
        if num_diff not in sum_dict:
            sum_dict[num_diff] = [num, i] # the number and the index of the number, using difference as key
        # ignore duplicates number, given for the case e.g. 14, and we got 7+7, the previous if statement will trigger.
    
    return [0,0] 