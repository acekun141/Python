"""
A fixed point in an array "A" is an index "i" such A[i] is equal to "i".

Given an array of "n" distinct integers sorted in ascending order, write a
function that returns a "fixed point" in the array. If there is not fixed
point return "None".
"""

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]

    return None


def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]

    return None

if __name__ == "__main__":
    A = [-1, 2, 5, 8, 17]
    B = [-15, -5, 0, 3, 6, 7]

    print(find_fixed_point(A))
    print(find_fixed_point(B))


