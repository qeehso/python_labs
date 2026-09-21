def transpose(mat: list[list[float | int]]) -> list[list]:
    """Возвращает транспонированную матрицу"""

    result = []

    if not mat:
        return []

    columns = len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    for j in range(len(mat[0])):
        row = []

        for i in range(len(mat)):
            row.append(mat[i][j])

        result.append(row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает сумму по каждой строке"""

    if not mat:
        return []
    
    result = []
    columns = len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    for row in mat:
        result.append(sum(row))

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    "Возвращает сумму по каждому столбцу"

    if not mat:
        return []
    
    result = []
    columns = len(mat[0])
    for row in mat:
        if len(row) != columns:
            raise ValueError('рваная матрица')

    for j in range(len(mat[0])):
        summa = 0
        for i in range(len(mat)):
            summa += mat[i][j]
        result.append(summa)

    return result
