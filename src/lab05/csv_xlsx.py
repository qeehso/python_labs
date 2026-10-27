from openpyxl import Workbook
import csv
from pathlib import Path
from src.lib.io_txt_csv import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''Конвертирует CSV файл в формат XLSX.

        Args:
            csv_path: Путь к исходному CSV файлу
            xlsx_path: Путь для сохранения XLSX файла

        Returns:
            None

        Raises:
            FileNotFoundError:
                Указанный CSV файл не найден
            ValueError:
                Указанный файл не формата CSV
                Файл CSV пустой
        '''
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if not csv_path.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if csv_path.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with csv_path.open('r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("Файл CSV пустой")

    wb = Workbook()
    ws = wb.active

    assert ws is not None
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_len = 0
        letter = col[0].column_letter

        for cell in col:
            if cell.value and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    ensure_parent_dir(xlsx_path)
    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")


