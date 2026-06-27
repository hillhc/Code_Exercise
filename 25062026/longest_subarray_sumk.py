'''
Write a function called longest_subarray that takes a list of positive numbers and a target k, and returns the length of the longest contiguous subarray whose sum is at most k (i.e. ≤ k).
For example:
longest_subarray([1, 2, 1, 0, 1, 1, 0], 4)   → 5    ([1,0,1,1,0] sums to 3, which is ≤ 4, length 5)
longest_subarray([2, 3, 1, 2], 5)            → 2    ([2,3] or [3,1]... [3,1] sums to 4 ≤5, length 2; [2,3]=5 ok too)
longest_subarray([5, 6, 7], 4)               → 0    (every element alone already exceeds 4)
longest_subarray([], 10)                     → 0    (empty)
'''

def longest_subarray(input_list, target):
    subarray_dict = {}
    current_sum = 0
    current_length = 0
    max_length = 0
    start_index = 0

    if len(input_list) == 0:
        return 0

    for i, num in enumerate(input_list):
        subarray_dict[i] = num # Each index storing the value of each index num
        current_length += 1
        current_sum += num
        
        while current_sum > target:
            current_sum -= subarray_dict[start_index]
            subarray_dict.pop(start_index)
            current_length -= 1
            start_index += 1

        if current_length > max_length and current_sum <= target:
            max_length = current_length

    return max_length