from src.lib.text import normalize, tokenize, count_freq, top_n
from pathlib import Path
import argparse

def run_cat(input_path: str, number_lines: bool = False) -> None:
    """Выводит содержимое файла построчной (с нумерацией при флаге -n)"""
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Указанный входной файл не найден: {input_path}")
    if not path.is_file():
        raise ValueError(f"Указанный путь не является файлом: {input_path}")

    with path.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            clean_line = line.rstrip("\r\n")
            if number_lines:
                print(f"{idx}: {clean_line}")
            else:
                print(clean_line)

def run_stats(input_path: str, top_count: int=5) -> None:
    """Анализирует частоты слов в тексте и выводит топ-N самых частых слов"""
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Указанный входной файл не найден: {input_path}")
    if not path.is_file():
        raise ValueError(f"Указанный путь не является файлом: {input_path}")

    raw_text = path.read_text(encoding="utf-8")
    norm_text = normalize(raw_text)
    tokens = tokenize(norm_text)

    if not tokens:
        raise ValueError("файл пустой")

    freq = count_freq(tokens)
    most_common = top_n(freq, top_count)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-{top_count}:")

    width = max((len(word) for word, _ in most_common), default=len("слово"))
    header = f"{'слово':<{width}} | частота"
    print(header)
    print("-" * len(header))

    for word, count in most_common:
        print(f"{word:<{width}} | {count}")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")


    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        run_cat(args.input, args.n)

    elif args.command == "stats":
        if args.top <= 0:
            stats_parser.error("Параметр --top должен быть положительным числом")
        run_stats(args.input, args.top)


if __name__ == "__main__":
    main()