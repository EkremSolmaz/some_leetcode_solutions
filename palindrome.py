def is_number_palindrome(num):
    initial_num = num
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = (num - num % 10) / 10

    return reverse == initial_num

assert is_number_palindrome(121) == True
assert is_number_palindrome(12345) == False
assert is_number_palindrome(98789) == True
assert is_number_palindrome(0) == True
assert is_number_palindrome(333) == True
assert is_number_palindrome(12321) == True
assert is_number_palindrome(112211) == True
assert is_number_palindrome(987654) == False
assert is_number_palindrome(121221) == False
assert is_number_palindrome(1001) == True
