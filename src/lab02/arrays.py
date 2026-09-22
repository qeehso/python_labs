def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if not nums:
        raise ValueError('Список не должен быть пустым')
    
    minimum = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):

        if nums[i] < minimum:
            minimum = nums[i]
        if nums[i] > maximum:
            maximum = nums[i]
            
    return minimum, maximum

    

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список уникальных значений по возрастанию

    """
    seen = []

    for num in nums:
        if num not in seen:
            seen.append(num)

    for i in range(len(seen)):
        min_ind = i

        for j in range(i + 1, len(seen)):
            if seen[j] < seen[min_ind]:
                min_ind = j

        seen[i], seen[min_ind] = seen[min_ind], seen[i]

    return seen


def flatten(mat: list[list | tuple]) -> list:
    "Возвращает одномерный список из многомерного"
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('строка не является строкой матрицы')
        
        for element in row:
            result.append(element)

    return result
