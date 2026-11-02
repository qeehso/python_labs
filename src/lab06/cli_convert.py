import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", help="Доступные подкоманды конвертации")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON-файл в формат CSV")
    p1.add_argument("--in", dest="input", required=True, help="Путь к исходному JSON-файлу")
    p1.add_argument("--out", dest="output", required=True, help="Путь для сохранения CSV-файла")

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV-файл в формат JSON")
    p2.add_argument("--in", dest="input", required=True, help="Путь к исходному CSV-файлу")
    p2.add_argument("--out", dest="output", required=True, help="Путь для сохранения JSON-файла")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV-файл в формат XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Путь к исходному CSV-файлу")
    p3.add_argument("--out", dest="output", required=True, help="Путь для сохранения XLSX-файла")

    args = parser.parse_args()

    if not args.cmd:
        parser.error("Не указана подкоманда. Используйте 'json2csv', 'csv2json' или 'csv2xlsx' (см. --help)")

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"Файл успешно сконвертирован в CSV: {args.output}")
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
        print(f'Файл успешно сконвертирован в JSON: {args.output}')
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f'Файл успешно сконвертирован в XLSX: {args.output}')


if __name__ == "__main__":
    main()