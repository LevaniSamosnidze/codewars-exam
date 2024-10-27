# 0) "Eureka" numbers (5 ქულა)

# The Eureka numbers are numbers like this: 135 = 1^1 + 3^2 + 5^3. Which means that we have to
#  take a number and sum its digits raised to the consecutive powers.
# First digit to power 1, second to power 2 and so on... If the result of that sum is the same
#  as the number itself that means that number is Eureka.

# Create a function which receives a range like (a, b) and outputs every Eureka number in it.

# NOTE: Every number which has one digit is Eureka, because for example 5 = 5^1...

# Examples:
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]


def Eureka_numbers(number, num):
    result = []
    for i in range(number, num):
        str_num = str(i)
        len1 = len(str_num)
        numbers_sum = 0
        for j in range(len1):
            l = str_num[j]
            numbers_sum += int(l) ** (j + 1)
        if i == numbers_sum:
            result.append(i)
    return result

print(Eureka_numbers(1, 100))
