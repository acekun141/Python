"""
Write a function that takes a non-negative integer and returns the largest
integer whose squre is less than or equal to the integer given.

Example
-------
    Assume input is integer 300.

    Then the expected output of the function should be 17,
    since 17^2 = 289 < 300. Note that 18^2 = 324 > 300,
    so the number is 17 is the correct response.
"""

def integer_square_root(k):
    low = 0
    high = k
    
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

if __name__ == "__main__":
    print(integer_square_root(300))
