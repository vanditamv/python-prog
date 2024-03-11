# check if string is palindrome
def is_str_palindrome(st):
    rev = st[::-1]
    if rev == st:
        print(f'{st} is palindrome')
    else:
        print(f'{st} is not a palindrome')


st = input("Enter a string ")
is_str_palindrome(st)
