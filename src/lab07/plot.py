import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def main():
    root = Path(__file__).resolve().parents[2]
    methods = ("bubble_sort", "insertion_sort", "selection_sort", "sorted")
    points = {method: [] for method in methods}
    with (root / "data/lab07/bench.csv").open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            if row["Task"] != "sort" or row["Method"] not in points:
                continue
            if row["Time"].startswith(">"):
                continue
            points[row["Method"]].append((int(row["Length"]), float(row["Time"])))

    fig, ax = plt.subplots(figsize=(10, 6))
    for method, marker in zip(methods, ("o", "s", "^", "D")):
        values = sorted(points[method])
        if values:
            sizes, times = zip(*values)
            ax.plot(sizes, times, marker=marker, linewidth=2, label=method)

    ax.set_yscale("log")
    ax.set_xticks(sorted({size for values in points.values() for size, _ in values}))
    ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    ax.set_xlabel("Размер списка, n")
    ax.set_ylabel("Время, с (логарифмическая шкала)")
    ax.set_title("Время сортировок в зависимости от размера списка")
    ax.grid(True, which="major", alpha=0.35)
    ax.grid(True, which="minor", axis="y", alpha=0.15)
    ax.legend()
    
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    output = root / "images/lab07/sorting_benchmark.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=180)
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
