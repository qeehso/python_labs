from pathlib import Path
import argparse
import sys

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

def main():
    parser = argparse.ArgumentParser(
        description = "Создание CSV-отчёта по частоте слов."
    )

    parser.add_argument(
        "--encoding",
        default ="utf-8",
        help="Кодировка входного файла (по умолчанию utf-8, например cp1251)"
    )

    parser.add_argument(
        "--in",
        dest="input_paths",
        nargs="+",
        type=Path,
        default=[ROOT_DIR / "data" / "lab04" / "input.txt"],
        help="Пути к входным файлам",
    )   

    parser.add_argument(
    "--out",
    dest="output_path",
    default=ROOT_DIR / "data" / "lab04" / "report.csv",
    type=Path,
    help="Путь к выходному CSV-файлу")

    parser.add_argument(
    "--per-file-out",
    type=Path,
    default=ROOT_DIR / "data" / "lab04" / "report_per_file.csv")

    parser.add_argument(
    "--total-out",
    type=Path,
    default=ROOT_DIR / "data" / "lab04" / "report_total.csv")

    args = parser.parse_args()

    # Обычный отчёт только по input.txt
    input_text = normalize(
        read_text(
            ROOT_DIR / "data" / "lab04" / "input.txt",
            encoding=args.encoding,
        )
    )
    input_tokens = tokenize(input_text)
    input_freq = count_freq(input_tokens)
    input_rows = top_n(input_freq, len(input_freq))


    per_file_rows = []
    total_freq = {}
    total_tokens = 0

    for input_path in sorted(args.input_paths, key=lambda path: path.name):
        if not input_path.is_absolute():
            input_path = ROOT_DIR / input_path

        text = normalize(read_text(input_path, encoding=args.encoding))
        tokens = tokenize(text)
        freq = count_freq(tokens)

        total_tokens += len(tokens)

        # Частоты слов для каждого файла
        for word, count in top_n(freq, len(freq)):
            per_file_rows.append((input_path.name, word, count))
            total_freq[word] = total_freq.get(word, 0) + count

    # Общие частоты по всем файлам
    total_rows = top_n(total_freq, len(total_freq))

    
    # Обычный отчёт
    write_csv(
        input_rows,
        path=args.output_path,
        header=("word", "count"),
    )

    # Отчёт по каждому файлу отдельно
    write_csv(
        per_file_rows,
        path=args.per_file_out,
        header=("file", "word", "count"),
    )

    # Сводный отчёт по всем файлам
    write_csv(
        total_rows,
        path=args.total_out,
        header=("word", "count"),
    )

    top_5 = top_n(total_freq)

    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {len(total_freq)}")
    print("Топ-5:")

    width = max(len(word) for word, count in top_5)
    
    print(f'{'слово':<{width}} | частота')
    print('-' * (width + 10))
    
    for word, count in top_5:
        print(f'{word:<{width}} | {count}')
    
if __name__ == '__main__':
    main()
