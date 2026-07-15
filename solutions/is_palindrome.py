# Is Palindrome
# Comprueba si un entero es palíndromo sin convertirlo a string.
#
# Fecha: 2026-07-15

def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10


if __name__ == '__main__':
    print(is_palindrome(121))   # True
    print(is_palindrome(-121))  # False
    print(is_palindrome(10))    # False
