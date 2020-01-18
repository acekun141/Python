def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        num += 26**count * ( ord(s) - ord('A') + 1)
        count -= 1 
    return num

if __name__ == "__main__":
    print(spreadsheet_encode_column("A"))
    print(spreadsheet_encode_column("AA"))
    print(spreadsheet_encode_column("ZZ"))
