from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает содержимое одной строкой
    
    Args:
        path: Путь к файлу в виде строки или объекта Path.
        encoding: Кодировка файла. По умолчанию используется UTF-8. 
            Для файлов в другой кодировке можно указать, например, encoding='cp1251'
            
    Returns:
        Содержимое файла в виде строки
    
    Raises:
        FileNotFoundError: Если файл не найден.
        UnicodeDecodeError: Если содержимой файла невозможно декодировать в указанной кодировке"""

    
    p = Path(path)

    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории, если они отсутствуют"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv( rows: Iterable[Sequence],
               path: str | Path, 
               header: tuple[str, ...] | None = None) -> None:
    """
    Записывает данные в csv файл.
    
    Создаёт родительские директории, если они отсутствуют.
    Если файл уже существует, его содержимое перезаписывается.

    Args:
        rows: итерируемый объект, содержащий строки данных. 
            Каждая строка должна быть последовательностью значений.
        path: путь к csv-файлу в виде строки или объекта Path.
        header: Необязательный кортеж с названиями столбцов.
            Если не указан, заголовок не записывается.

    Raises:
        OSError: если ен удалось создать директории или записать файл.
        ValueError: Если строки имеют разную длину или длина
            заголовка не совпадает с длиной строк данных.
    """
    rows = list(rows)

    if rows:
        expected_length = len(rows[0])

        for index, row in enumerate(rows, start=1):
            if len(row) != expected_length:
                raise ValueError(
                    f"Строка {index} содержит {len(row)} значений, "
                    f"ожидалось {expected_length}."
                )

    if header is not None and len(header) != expected_length:
        raise ValueError(
            f"Заголовок содержит {len(header)} столбцов, "
            f"ожидалось {expected_length}."
        )
    
    p = Path(path)

    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)



# print(read_text(r"C:\Users\никита\python_labs\data\lab04\input.txt", encoding="utf-8"))
# txt = read_text(r"C:\Users\никита\python_labs\data\lab04\input.txt")  # должен вернуть строку
# write_csv([("word","count"),("test",3)], "data/check.csv", header= (["что-то"]))  # создаст CSV
