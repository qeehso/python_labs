from pathlib import Path
import csv
from typing import Iterable, Sequence
import argparse

from lib.text import normalize, tokenize, count_freq, top_n
from .io_txt_csv import read_text, ensure_parent_dir, write_csv

def main():
    parser = argparse.ArgumentParser(
        description = "Создание CSV-отчёта по частоте слов."
    )
    parser.add_argument(
        "--encoding",
        default ="utf-8",
        help="Кодировка входного файла (по умолчанию utf-8, например cp1251)"
    )
    args = parser.parse_args()

    text = read_text(path="../data/lab04/input.txt", encoding=args.encoding)

    text = normalize(text)
    tokens = tokenize(text)
    text_freq = count_freq(tokens)
    top_5 = top_n(text_freq)
    top = top_n(text_freq, n=len(tokens))

    write_csv(top,
               path="../data/report.csv", 
               header= ("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(text_freq)}")
    print("Топ-5:")

    if top_5:
        width = max(len(word) for word, count in top_5)

        print(f"{'слово':<{width}} | частота")
        print("-" * (width + 10))

        for word, count in top_5:
            print(f"{word:<{width}} | {count}")
    
if __name__ == '__main__':
    main()
