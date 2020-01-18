def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False
    
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

    for i in ht:
        if ht[i] != 0:
            return False

    return True

if __name__ == "__main__":
    s1 = str(input("Frist String: "))
    s2 = str(input("Second String: "))
    print(is_anagram(s1.replace(" ", "").lower(),
                     s2.replace(" ", "").lower()))
