def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись студента в виде строки.

    ФИО должно содержать фамилию и имя или фамилию, имя и отчество.
    Лишние пробелы удаляются.

    Raises:
        TypeError: если rec не является tuple, ФИО или группа пустые,
            либо GPA имеет неверный тип.
        ValueError: если tuple имеет неверную длину, ФИО содержит
            неверное количество слов или GPA находится вне диапазона 0..5 
    """

    if not isinstance(rec, tuple):
        raise TypeError("Не тот тип входных данных: нужен tuple")

    if len(rec) != 3:
        raise ValueError("Неправильная длина кортежа")

    if not rec[0].strip():
        raise TypeError("Пустое ФИО")

    if not rec[1].strip():
        raise TypeError("Пустая группа")

    if not isinstance(rec[2], (int, float)):
        raise TypeError("Неверный тип GPA (GPA должен быть float или int)")

    if rec[2] < 0 or rec[2] > 5:
        raise ValueError('GPA должно быть от 0 до 5')

    if len(rec[0].split()) != 3 and len(rec[0].split()) != 2: 
        raise ValueError('либо ФИ, либо ФИО')



    fio = rec[0]
    group = 'гр. ' + rec[1].strip()
    gpa = f'GPA {rec[2]:.2f}'

    words = fio.split()
    initials = words[0].capitalize() + ' '
        
    for word in words[1:]:
        initials += word[0].upper() + '.'
        

    return f'{initials}, {group}, {gpa}'



# Тест кейсы
print(
    f'format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) ->',
    format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
)

print(
    f'format_record(("Петров Пётр", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр", "IKBO-12", 5.0))
)

print(
    f'format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) ->',
    format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
)

print(
    f'format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) ->',
    format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
)

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
