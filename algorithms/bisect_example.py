""""
Bisect:
    - "Built-in" binary search method in Python.
    - Can be used to search for an element i a sorted list.
"""

# Import allows us to make use of the bisect module.
import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# The bisect_left function finds index of the target element.
# In the event where there are dupliate entries satisfying the target element,
# the bisect_left function returns the left most occurence.

# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurence of 285 is at index 6
print(bisect.bisect_left(A, 285))

# The bisect_right function returns the insertion point which comes after, or
# to the right of, any exiting entries in the list.

# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10))

# Index position after last occurence of 285 is 9
print(bisect.bisect_right(A, 285))

# There is also just a regular default "bisect" function. This function is
# equivalent to "bisect_right":

# Index position to right of -10 is 2. (Same as bisect right)
print(bisect.bisect(A, -10))
