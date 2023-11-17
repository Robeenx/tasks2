"""
Нас интересует сбор наборов из шести простых чисел, в которых, имея начальное простое число p,
следующие значения также являются простыми числами, образующими шестерня.
[p, p + 4, p + 6, p + 10, p + 12, p + 16]

Первый секступлет, который мы находим, это [7, 11, 13, 17, 19, 23]

Второй [97, 101, 103, 107, 109, 113]

Учитывая число sum_limit, вы должны указать первый секступлет, сумма которого
(из шести простых чисел) превышает значение sum_limit.

find_primes_sextuplet(70) == [7, 11, 13, 17, 19, 23]

find_primes_sextuplet(600) == [97, 101, 103, 107, 109, 113]

Особенности тестов:

Number Of Tests = 18
10000 < sum_limit < 29700000

"""


def is_prime(num: int) -> bool:
    """
    Проверяет является ли число простым. (начиная от 3)
    """
    return all(num % n for n in range(3, int(num ** .5 + 1), 2))


def find_primes_sextuplet(sum_limit: int) -> list[int] | None:
    """
    Поиск простой шестеренки, большей по сумме заданного числа.
    """
    for x in range(3, sum_limit, 2):
        if is_prime(x):
            if next((0 for i in (4, 6, 10, 12, 16) if not is_prime(x + i)), 1):
                if sum_limit < sum(tmp := [x + i for i in (0, 4, 6, 10, 12, 16)]):
                    return tmp
    return None


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (70, [7, 11, 13, 17, 19, 23]),
        (600, [97, 101, 103, 107, 109, 113]),
        (2000000, [1091257, 1091261, 1091263, 1091267, 1091269, 1091273]),
    )
    for key, val in data:
        assert find_primes_sextuplet(key) == val


if __name__ == '__main__':
    test()