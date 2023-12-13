"""
# Activity Selector
Given the start and finish times of m different activities, find the longest
subsequence of activities that can be planned without any overlapping.
"""

# i | 1 2 3 4 5 6 7  8  9  10 11
# ______________________________
# si| 1 3 0 5 3 5 6  8  8  2  12
# fi| 4 5 6 7 9 9 10 11 12 14 16

# The largest valid subset is {a1, a4, a8, a11}
#from typing import Union

# activities set
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# iterative O(n) implementation
def activity_selector(s, f, a):
    pass


# recursive O(n) implementation
def activity_selector_recursive(a, s, f):
    pass


# s: start time
# f: finish time
# i: activity index
# n: total size
def activity_selector_recursive_helper(s, f, i, n, a):
    pass