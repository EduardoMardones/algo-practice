# Maximum Subarray
# Encuentra la suma máxima de un subarreglo contiguo (algoritmo de Kadane).
#
# Fecha: 2026-10-21

def max_subarray(nums: list[int]) -> int:
    max_sum = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        max_sum = max(max_sum, current)
    return max_sum


if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))                                # 1
    print(max_subarray([5, 4, -1, 7, 8]))                  # 23
