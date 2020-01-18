"""
You are given some numeric string as input. Convert the string you are given
to an integer. Do not make use of the built-in "int" function.

Example
-------
    "123" -> 123
    "-12332" -> -12332
    "554" -> 554
"""

def str_to_int(input_str):
    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True 
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    return output_int

if __name__ == "__main__":
    input_str = str(input("String Numbers: "))
    print(type(input_str))
    print(str_to_int(input_str))
    print(type(str_to_int(input_str)))

