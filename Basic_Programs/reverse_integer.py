'''Given a 32-bit signed integer, reverse digits of an integer.
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21 '''

def reverse_integer(num):
    temp = num
    reversed = 0
    sign = 1 if num >= 0 else -1

    num = abs(num)
    while num > 0 :
        rem = num %10
        reversed = reversed *10 + rem
        num = num //10

    return reversed
  

# Example usage:
print(reverse_integer(123))  # Output: 321
print(reverse_integer(-123))  # Output: -321
print(reverse_integer(120))  # Output: 21
