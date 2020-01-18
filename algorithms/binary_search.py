data = [2, 4, 5, 6, 7, 8, 14, 17, 19, 22, 28, 32]
target = 6

# Linear Search
def linear_search(data, target):
    for value in data:
        if value == target:
            return True
    return False

# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


if __name__ == "__main__":
    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) -1))
