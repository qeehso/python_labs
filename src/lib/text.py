import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст:

    Приводит к нижнему регистру, заменяет ё на е и
    нормализует последовательности пробельных символов до одного пробела.

    Параметры:
        text: Исходный текст.
        casefold: Использовать casefold() вместо lower().
        yo2e: Заменять символы ё и Ё на е.

    Возвращает:
        Нормализованный текст.
    """
    
    if casefold:
        text = text.casefold()
    else: 
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е')

    text = text.strip()
    text = ' '.join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на токены.

    Токеном считается последовательность букв, цифр или символов
    подчёркивания. Дефис внутри токена сохраняется.

    Параметры:
        text: Исходный текст.

    Возвращает:
        Список токенов.
    """

    text = re.findall(r"\w+(?:-\w+)*", text)

    return text


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
        Подсчитывает частоту каждого токена.
    
        Параметры:
            tokens: Список токенов.
    
        Возвращает:
            Словарь, где ключ - это токен, а значение - это его частота.
        """   
     
    freq = {}

    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1


    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает n наиболее часто встречающихся токенов.

    Сначала токены сортируются по убыванию частоты.
    При одинаковой частоте используется алфавитный порядок токенов.

    Параметры:
        freq: Словарь с частотами токенов.
        n: Количество токенов, которые нужно вернуть.

    Возвращает:
        Список пар (токен, частота).
    """

    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]




# тест кейсы:
# normalize
# print(f'normalize({repr("ПрИвЕт\nМИр\t")}) -> {normalize("ПрИвЕт\nМИр\t")}')
# print(f'normalize({repr("ёжик, Ёлка")}) -> {normalize("ёжик, Ёлка")}')
# print(f'normalize({repr("Hello\r\nWorld")}) -> {normalize("Hello\r\nWorld")}')
# print(f'normalize({repr("  двойные   пробелы  ")}) -> {normalize("  двойные   пробелы  ")}')

# tokenize
# print(f'tokenize({repr("привет мир")}) -> {tokenize("привет мир")}')
# print(f'tokenize({repr("hello,world!!!")}) -> {tokenize("hello,world!!!")}')
# print(f'tokenize({repr("по-настоящему круто")}) -> {tokenize("по-настоящему круто")}')
# print(f'tokenize({repr("2025 год" )}) -> {tokenize("2025 год" )}')
# print(f'tokenize({repr("emoji 😀 не слово")}) -> {tokenize("emoji 😀 не слово")}')

# freq_count
# print(f'count_freq(["a","b","a","c","b","a"]) -> {count_freq(["a","b","a","c","b","a"])}')
# print(f'count_freq(["bb","aa","bb","aa","cc"]) -> {count_freq(["bb","aa","bb","aa","cc"])}')

# top_n
# print(f'top_n({repr({"a":3,"b":2,"c":1})}, n=2) -> {top_n({"a":3,"b":2,"c":1}, n=2)}')
# print(f'top_n({repr({"aa":2,"bb":2,"cc":1})}, n=2) -> {top_n({"aa":2,"bb":2,"cc":1}, n=2)}')

