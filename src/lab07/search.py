def linear_search(nums, x):
    """Индекс первого вхождения x или -1.
 
    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for idx in range(len(nums)):
        if nums[idx] == x:
            return idx
    return -1


def binary_search(sorted_nums, x):
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
 
    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    left = 0
    right = len(sorted_nums) - 1

    while left <= right: 
        mid = (left + right) // 2

        if x == sorted_nums[mid]:
            return mid
        elif x < sorted_nums[mid]:
            right = mid - 1
        elif x > sorted_nums[mid]:
            left = mid + 1 
    return -1


def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.
 
    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def two_sum_fast(nums, target):
    """Хранит в словаре seen число и его индекс, 
    в цикле считаем разницу с таргетом, и если оно
    уже встречалось в seen, то возвращаем индекс числа из seen и текущий i
    
    two_sum_fast([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_fast([1, 2], 10) -> None
    """
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return seen[complement], i
        seen[x] = i
    return None
