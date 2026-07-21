# Climbing Stairs
# Número de formas distintas de subir n escalones (1 o 2 por vez). DP clásico.
#
# Fecha: 2026-07-21

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    for i in range(1, 8):
        print(f'climb_stairs({i}) = {climb_stairs(i)}')
