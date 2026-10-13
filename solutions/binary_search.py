# Binary Search
# Implementación iterativa de búsqueda binaria en O(log n).
#
# Fecha: 2026-10-13

def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    arr = [-1, 0, 3, 5, 9, 12]
    print(binary_search(arr, 9))   # 4
    print(binary_search(arr, 2))   # -1
