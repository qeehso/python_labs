from pathlib import Path
import argparse
import sys

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

DATA_DIR = ROOT_DIR / "data" / "lab04"


def main():
    parser = argparse.ArgumentParser(description="Создание CSV-отчёта по частоте слов.")
    parser.add_argument("--encoding", default="utf-8", help="Кодировка, например cp1251")
    parser.add_argument("--in", dest="input_paths", nargs="+", type=Path,
                        default=[DATA_DIR / "input.txt"], help="Входные файлы")
    parser.add_argument("--out", dest="output_path", type=Path,
                        default=DATA_DIR / "report.csv", help="Обычный отчёт")
    parser.add_argument("--per-file", dest="per_file_out", type=Path,
                        default=DATA_DIR / "report_per_file.csv")
    parser.add_argument("--total", dest="total_out", type=Path,
                        default=DATA_DIR / "report_total.csv")
    args = parser.parse_args()

    # Обычный отчёт по input.txt
    text = normalize(read_text(DATA_DIR / "input.txt", encoding=args.encoding))
    input_freq = count_freq(tokenize(text))
    write_csv(top_n(input_freq, len(input_freq)), path=args.output_path,
              header=("word", "count"))

    # Обработка входных файлов
    per_file_rows, total_freq, total_tokens = [], {}, 0

    for path in sorted(args.input_paths, key=lambda p: p.name):
        if not path.is_absolute():
            path = ROOT_DIR / path

        tokens = tokenize(normalize(read_text(path, encoding=args.encoding)))
        freq = count_freq(tokens)
        total_tokens += len(tokens)

        for word, count in top_n(freq, len(freq)):
            per_file_rows.append((path.name, word, count))
            total_freq[word] = total_freq.get(word, 0) + count

    # Запись отчётов
    write_csv(per_file_rows, path=args.per_file_out,
              header=("file", "word", "count"))
    write_csv(top_n(total_freq, len(total_freq)), path=args.total_out,
              header=("word", "count"))

    # Статистика
    top_5 = top_n(total_freq)
    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {len(total_freq)}")
    print("Топ-5:")

    width = max((len(word) for word, _ in top_5), default=len("слово"))
    header = f"{'слово':<{width}} | частота"
    print(header)
    print("-" * len(header))

    for word, count in top_5:
        print(f"{word:<{width}} | {count}")


if __name__ == "__main__":
    main()
