"""
Given an array of sorted integers. We need to find the closest value to the
given number.

Array may contain duplicate values and negative numbers.

Example
-------
Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}

Target number = 11
Ouput : 9
9 is closest to 11 is given array
"""

def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    # Edge cases for emtpy list or when the list is only the one element
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        # Ensure we don't read beyound the bound of the list
        # And obtain the left and right difference values
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)
        # Check if the absolute value between left and right elements are
        # smaller than any seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
        # Move the mid-point accordingly as is done via binary search.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # If the element is the target itself, the closest number to it is
        # itself
        else:
            return A[mid]
    
    return closest_num


if __name__ == "__main__":
    A = [1, 2, 4, 5, 6, 6, 8, 9]
    B = [2, 5, 6, 7, 8, 8, 9]

