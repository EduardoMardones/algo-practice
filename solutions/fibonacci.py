# Fibonacci Memoized
# Calcula el n-ésimo número de Fibonacci con memoización para O(n).
#
# Fecha: 2026-08-20

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for i in range(10):
        print(f'fib({i}) = {fib(i)}')
