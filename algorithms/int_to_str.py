"""
You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2 ,3, ...)

Convert the integer you are given to a string. Do not make use of the built-in
"str" function.

Example
-------
    Input : 123
    Output : "123"
"""

def int_to_str(input_int):
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else: 
        is_negative = False

    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10))
        input_int //= 10
        
    return ''.join(output_str[::-1])

if __name__ == "__main__":
    input_int = int(input('Integer: '))
    print(int_to_str(input_int))
