#To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.

def code_at(row, col):
    start = 20151125
    mult = 252533
    mod = 33554393

    diagonal = row + col - 1
    codes_before = (diagonal - 1) * diagonal // 2
    index = codes_before + col - 1  # 0-based index

    # modular exponentiation
    code = (start * pow(mult, index, mod)) % mod
    return code

# Example: find code at row=6, col=6 from your table
row, col = 2981, 3075
print(code_at(row, col))
