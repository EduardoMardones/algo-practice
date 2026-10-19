# Reverse String
# Invierte una cadena de texto in-place usando dos punteros.
#
# Fecha: 2026-10-19

def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    chars = ['h', 'e', 'l', 'l', 'o']
    reverse_string(chars)
    print(chars)  # ['o', 'l', 'l', 'e', 'h']
