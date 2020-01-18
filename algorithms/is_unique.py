"""
Implement an algorithm to determine if a string has all unique characters.
"""

def normalize(s):
    s = s.replace(" ","")
    
    return s.lower()

def is_unique_1(s):
    ht = dict()
    for i in s:
        if i in ht:
            return False
        else:
            ht[i] = 1 
    return True


def is_unique_2(s):
    return len(set(s)) == len(s)


def is_unique_3(s):
    ALPHA = "abcdefghijklmnopqrstuvwxyz"

    for i in s:
        if i in ALPHA:
            ALPHA = ALPHA.replace(i, "")
        else:
            return False
    return True

if __name__ == "__main__":
    unique_str =  "AbCDeFT"
    non_unique_str = "non Unique StR"
    print("Using first function")
    print(is_unique_1(normalize(unique_str)))
    print(is_unique_1(normalize(non_unique_str)))
    print("Using second function")
    print(is_unique_2(unique_str))
    print(is_unique_2(non_unique_str))
    print("Using third funtion")
    print(is_unique_3(normalize(unique_str)))
    print(is_unique_3(normalize(non_unique_str)))



