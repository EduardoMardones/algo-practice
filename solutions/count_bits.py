# Counting Bits
# Para cada número de 0 a n, cuenta cuántos bits 1 tiene. DP en O(n).
#
# Fecha: 2026-10-14

def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


if __name__ == '__main__':
    print(count_bits(5))   # [0, 1, 1, 2, 1, 2]
    print(count_bits(2))   # [0, 1, 1]
