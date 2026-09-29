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

# Тест кейсы
# min_max
print(f'min_max([3, -1, 5, 5, 0]) ->', min_max([3, -1, 5, 5, 0]))
print(f'min_max([42]) ->', min_max([42]))
print(f'min_max([-5, -2, -9]) ->', min_max([-5, -2, -9]))
print(f'min_max([1.5, 2, 2.0, -3.1]) ->', min_max([1.5, 2, 2.0, -3.1]))

try:
    print(f'min_max([]) ->', min_max([]))
except ValueError as error:
    print(f'min_max([]) -> ValueError: {error}')

# unique_sorted
print(f'unique_sorted([3, 1, 2, 1, 3]) ->', unique_sorted([3, 1, 2, 1, 3]))
print(f'unique_sorted([]) ->', unique_sorted([]))
print(f'unique_sorted([-1, -1, 0, 2, 2]) ->', unique_sorted([-1, -1, 0, 2, 2]))
print(f'unique_sorted([1.0, 1, 2.5, 2.5, 0]) ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))

# flatten
print(f'flatten([[1, 2], [3, 4]]) ->', flatten([[1, 2], [3, 4]]))
print(f'flatten([[1, 2], (3, 4, 5)]) ->', flatten([[1, 2], (3, 4, 5)]))
print(f'flatten([[1], [], [2, 3]]) ->', flatten([[1], [], [2, 3]]))

try:
    print(f'flatten([[1, 2], "ab"]) ->', flatten([[1, 2], "ab"]))
except TypeError as error:
    print(f'flatten([[1, 2], "ab"]) -> TypeError: {error}')

