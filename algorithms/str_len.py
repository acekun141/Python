# Given a string, calculate the length of the string.

input_str = "LeVietHung"

def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

if __name__ == "__main__":
    print(recursive_str_len(input_str))
