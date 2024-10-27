# 7) Fibonacci Sequence Generator (4 ქულა)
# Create a program that receives an integer n and returns the first n numbers 
# in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is
#  the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]


def Fibonacci_Sequence_Generator(number):
    result = [0,1]
    for i in range(number):
        result.append(result[i] + result[i+1])
    
    return result[:number]
    

print(Fibonacci_Sequence_Generator(5))