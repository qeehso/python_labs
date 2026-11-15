import random
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100) -> None:
    """Сравнить сортировку со встроенной sorted."""
    rng = random.Random(42)
    for _ in range(trials):
        nums = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
        original = nums.copy()
        result = fn(nums)
        assert result == sorted(original), fn.__name__
        assert nums == original, fn.__name__
        assert result is not nums, fn.__name__


def check_search(trials=100) -> None:
    """Проверить индексы, возвращаемые поиском"""
    rng = random.Random(42)
    for _ in range(trials):
        nums = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
        x = rng.randint(-100, 100)
        expected = nums.index(x) if x in nums else -1
        assert linear_search(nums, x) == expected

        ordered = sorted(nums)
        index = binary_search(ordered, x)
        if x in ordered:
            assert 0 <= index < len(ordered)
            assert ordered[index] == x
        else:
            assert index == -1


def check_two_sum(trials=100) -> None:
    """Сравнить решение со словарём с перебором"""
    rng = random.Random(42)
    for _ in range(trials):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(0, 50))]
        target = rng.randint(-20, 20)
        expected = two_sum_brute(nums, target)
        result = two_sum_fast(nums, target)
        if expected is None:
            assert result is None
        else:
            assert result is not None
            for i, j in (expected, result):
                assert 0 <= i < j < len(nums)
                assert nums[i] + nums[j] == target


def main() -> None:
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены")


if __name__ == "__main__":
    main()
