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
