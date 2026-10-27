import json
import csv
from pathlib import Path
from src.lib.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Записывает значения

    Args:
        json_path: Путь к json файлу из которого читаем
        csv_path: Путь к csv файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный JSON файл не найден
        ValueError:
            Указанный файл не формата JSON
            Пустой JSON или неподдерживаемая структура
            Файл JSON пустой или имеет неправильный формат
            Все элементы списка JSON должны быть словарями
    '''
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not json_path.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if json_path.suffix.lower() != '.json':
        raise ValueError("Указанный файл не формата JSON")

    try:
        with json_path.open('r', encoding='utf-8') as p:
            data = json.load(p)
    except json.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(csv_path)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with csv_path.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Записывает значения

    Args:
        csv_path: Путь к csv файлу из которого читаем
        json_path: Путь к json файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный CSV файл не найден
        ValueError:
            Указанный файл не формата CSV
            Файл CSV пустой
            Файл CSV не содержит данных
    '''
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if csv_path.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")

        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(json_path)
    with json_path.open('w', encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")