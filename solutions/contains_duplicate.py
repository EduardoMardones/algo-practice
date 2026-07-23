# Contains Duplicate
# Retorna True si algún valor aparece al menos dos veces en el arreglo.
#
# Fecha: 2026-07-23

def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))     # True
    print(contains_duplicate([1, 2, 3, 4]))     # False
    print(contains_duplicate([1, 1, 1, 3, 3]))  # True
