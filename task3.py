a = input('Enter a String: ')
b = a[::-1]
if b == a:
    print(f'{b} is a Palindrome')
else:
    print(f'{b} is not a Palindrome')
