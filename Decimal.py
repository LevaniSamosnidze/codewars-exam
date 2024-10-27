#  Decimal --> Binary Conversion (2 ქულა)

# Create a program which receives a decimal number and converts it to binary.

# Examples:
# 17 --> 10001
# 15 --> 1111


def decimal(numebr):
    res = bin(numebr)[2:]
    return res

print(decimal(5))
