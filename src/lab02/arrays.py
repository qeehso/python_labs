def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Возвращает кортеж, содержащий минимальное и максимальное значение из списка чисел

    """
    if not nums:
        raise ValueError("Список не должен быть пустым")
    
    min_value = min(nums)
    max_value = max(nums)

    return min_value, max_value

    

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список уникальных значений по возрастанию

    """
    
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    "Возвращает одномерный список из многомерного"
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('строка не является строкой матрицы')
        
        for element in row:
            result.append(element)

    return result

