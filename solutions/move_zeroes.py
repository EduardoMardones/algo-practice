# Move Zeroes
# Mueve todos los ceros al final del arreglo manteniendo el orden relativo.
#
# Fecha: 2026-07-27

def move_zeroes(nums: list[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)  # [1, 3, 12, 0, 0]
