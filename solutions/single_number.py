# Single Number
# Encuentra el único elemento no repetido en un arreglo usando XOR.
#
# Fecha: 2026-08-14

def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result


if __name__ == '__main__':
    print(single_number([2, 2, 1]))       # 1
    print(single_number([4, 1, 2, 1, 2])) # 4
    print(single_number([1]))             # 1
