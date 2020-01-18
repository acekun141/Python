"""
Given two strings, write a method to decide if one is a permutaion of the
other.
"""

# Time Complexity: 0 (n log n)
# Space Complexity: 0(1)
def is_perm_1(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    return True

def is_perm_2(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    ht = dict()

    for i in s1:
        if i in ht:
            ht[i] += 1
        else: 
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for _, v in ht.items():
        if v != 0:
            return False
    
    return True

if __name__ == "__main__":
    is_permutation_1 = "Not"
    is_permutation_2 = "ton"

    not_permutation_1 = "Not"
    not_permutation_2 = "Top"

    print(is_perm_1(is_permutation_1, is_permutation_2))
    print(is_perm_1(not_permutation_1, not_permutation_2))

    print(is_perm_2(is_permutation_1, is_permutation_2))
    print(is_perm_2(not_permutation_1, not_permutation_2))
