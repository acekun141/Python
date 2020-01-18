"""
Given a string, count the number of consonants.
Note: a consonant is a letter that is not a vowel,
i.e. a letter that is not a,e,i,o, and u.
"""

VOWEL = "aeiou"

def iterative_count_consonants(input_str):
    count = 0
    for letter in input_str:
        if (letter.lower() not in VOWEL and
                letter.isalpha()):
            count += 1
    return count


def recursive_count_consonants(input_str):
    if input_str == '':
        return 0
    
    if (input_str[0].lower() not in VOWEL and
            input_str[0].isalpha()):
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


if __name__ == "__main__":
    input_str = str(input('Input String: '))
    print(iterative_count_consonants(input_str))
    print(recursive_count_consonants(input_str))
