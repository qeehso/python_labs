def format_record(rec: tuple[str, str, float]) -> str:
    """Возвращает форматированную строку из кортежа
    В формате: g"""


    if not rec[0].strip():
        raise TypeError("Пустое ФИО")

    if not rec[1].strip():
        raise TypeError("Пустая группа")

    if not isinstance(rec[2], (int, float)):
        raise TypeError("Неверный тип GPA (GPA должен быть float или int)")

    fio = rec[0]
    group = 'гр. ' + rec[1].strip()
    gpa = f'GPA {rec[2]:.2f}'

    words = fio.split()
    initials = words[0].capitalize() + ' '
        
    for word in words[1:]:
        initials += word[0].upper() + '.'
        

    return f'{initials}, {group}, {gpa}'
