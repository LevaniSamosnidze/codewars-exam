# 9) Prime time (4 ქულა)

# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]

def prime_time(num):
    result = []
    if num > 2:
        result.append(2)
    if num > 3:
        result.append(3)
    for num in range(2, num + 1):
        if num % 2 != 0 and num % 3 != 0:
            result.append(num)
    return result

print(prime_time(11))