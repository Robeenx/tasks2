"""
Задача:
Вам даны два числа aи bгде 0 ≤ a ≤ b.
Представьте, что вы создаете массив всех целых чисел из a к b включительно.
Вам необходимо посчитать количество 1s в двоичном представлении всех чисел
массива.

Пример:
Для a = 2 и b = 7 выход должен быть 11

Учитывая a = 2 и b = 7, массив имеет вид: [2, 3, 4, 5, 6, 7].
Преобразовав числа в двоичные, получим [10, 11, 100, 101, 110, 111],
в котором содержится 1 + 2 + 1 + 2 + 2 + 3 = 11 единиц.
"""


def range_bit_count(a: int, b: int) -> int:
    """
    Подсчитывает кол-во единиц в двоичной системе из диапазона чисел (a, b)
    включительно.
    """
    return len(''.join(f'{x:b}'.replace('0', '') for x in range(a, b + 1)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((2, 7), 11),
        ((0, 1), 1),
        ((4, 4), 1),
    )
    for key, val in data:
        assert range_bit_count(*key) == val


if __name__ == '__main__':
    test()
