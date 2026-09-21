def initials_fio(fio: str) -> str:
    """Возвращает инициалы"""

    words = fio.split()
    initials = words[0].capitalize() + ' '

    for word in words[1:]:
        initials += word[0].upper() + '.'

    return initials


def format_record(rec: tuple[str, str, float]) -> str:
    """Возвращает форматированную строку из кортежа
    В формате: Иванов И.И., гр. BIVT-26, GPA 5.00"""

    if not rec[0].strip():
        raise TypeError("Пустое ФИО")

    if not rec[1].strip():
        raise TypeError("Пустая группа")

    if not isinstance(rec[2], (int, float)):
        raise TypeError("Неверный тип GPA (GPA должен быть float или int)")


    fio = initials_fio(rec[0])
    group = 'гр. ' + rec[1].strip()
    gpa = f'GPA {rec[2]:.2f}'

    return f'{fio}, {group}, {gpa}'


print(f'format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) ->',
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(f'format_record(("Петров Пётр", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(f'format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(f'format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) ->',
    format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

try:
    print(
        f'format_record(("", "BIVT-25", 4.6)) ->',
        format_record(("", "BIVT-25", 4.6))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("", "BIVT-25", 4.6)) -> {type(error).__name__}: {error}')

try:
    print(
        f'format_record(("Иванов Иван", "", 4.6)) ->',
        format_record(("Иванов Иван", "", 4.6))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван", "", 4.6)) -> {type(error).__name__}: {error}')

try:
    print(
        f'format_record(("Иванов Иван", "BIVT-25", "4.6")) ->',
        format_record(("Иванов Иван", "BIVT-25", "4.6"))
    )
except (ValueError, TypeError) as error:
    print(f'format_record(("Иванов Иван", "BIVT-25", "4.6")) -> {type(error).__name__}: {error}')