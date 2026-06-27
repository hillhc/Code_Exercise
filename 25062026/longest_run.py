"""
Write a function called longest_run that takes a list and returns the length of the longest run of consecutive equal elements.
For example:
longest_run([1, 1, 2, 3, 3, 3, 1])   → 3    (the run of three 3s)
longest_run([5, 5, 5, 5])            → 4    (all four 5s in a row)
longest_run([7, 8, 9])               → 1    (no repeats, longest run is just 1)
longest_run([])                      → 0    (empty list)
"""

def longest_run(input_list):
    current_num = None
    run_length = 0
    max_length = 0

    if len(input_list) == 0: # Handling empty list
        return 0
    
    for num in input_list:
        if current_num == None: # Initialization
            current_num = num
            run_length = 1
        elif current_num != num: # Stop of consecutive run
            if run_length > max_length: # Update max_length
                max_length = run_length 
            run_length = 1
            current_num = num
        else:
            run_length += 1
    if run_length > max_length:
        max_length = run_length

    return max_length
