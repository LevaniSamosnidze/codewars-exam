# 1) Binary --> Decimal Conversion (2 ქულა)

# Create a program which receives a binary number and converts it to decimal.

# Examples:
# 10001 --> 17
# 1111 --> 15


def binary(num):
    number = 0
    l = 0
    
    for i in num[::-1]:
        number += int(i) * (2 ** l)
        l += 1
    
    return number

print(binary('1500'))