"""Построить график сортировок по сохранённому bench.csv."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    root = Path(__file__).resolve().parents[2]
    methods = ("bubble_sort", "insertion_sort", "selection_sort", "sorted")
    with (root / "data/lab07/bench.csv").open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    rows.sort(key=lambda row: int(row["Length"]))

    plt.figure(figsize=(10, 6))
    for method in methods:
        sizes = []
        times = []
        for row in rows:
            if row["Task"] == "sort" and row["Method"] == method:
                if row["Time"].startswith(">"):
                    continue
                sizes.append(int(row["Length"]))
                times.append(float(row["Time"]))
        plt.plot(sizes, times, marker="o", label=method)

    plt.yscale("log")
    plt.xlabel("Размер списка, n")
    plt.ylabel("Время, с (логарифмическая шкала)")
    plt.title("Время сортировок в зависимости от размера списка")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    output = root / "images/lab07/sorting_benchmark.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=180)
    plt.close()
    print(output)


if __name__ == "__main__":
    main()
