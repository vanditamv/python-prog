# check number is a palindrome or not
# 2002 -> palindrome, 2001 -> not a palindrome

def is_palindrome(num):
    rev = 0
    temp = num

    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num = num // 10

    if rev == temp:
        print(f'{temp} is a Palindrome')
    else:
        print(f'{temp} is NOT a Palindrome')

number = int(input("Enter a number "))
is_palindrome(number)
