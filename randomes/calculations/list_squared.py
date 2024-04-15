"""
1, 246, 2, 123, 3, 82, 6, 41являются делителями числа 246.
Возведя эти делители в квадрат, получим: 1, 60516, 4, 15129, 9, 6724, 36, 1681.
Сумма этих квадратов равна 84100который 290 * 290.
Задача

Найдите все целые числа между mи n(m и n целых чисел с 1 <= m <= n) такие,
что сумма их квадратов делителей сама является квадратом.

Мы вернем массив подмассивов или кортежей (в C — массив пар) или строку.
Подмассивы (или кортежи, или пары) будут состоять из двух элементов:
сначала числа, квадраты делителей которого являются квадратами,
а затем сумма квадратов делителей.
Пример:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""


def list_squared(a: int, b: int) -> list:
    """
    Поиск чисел, квадрат суммы делителей которого, так же является квадратом, из заданного диапазона.
    """
    return [[i, x] for i in range(a, b+1) if ((x := sum(x ** 2 for x in range(1, i + 1) if not i % x)) ** .5).is_integer()]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((1, 250), [[1, 1], [42, 2500], [246, 84100]]),
        ((42, 250), [[42, 2500], [246, 84100]]),
        ((250, 500), [[287, 84100]]),
    )
    for key, val in data:
        assert list_squared(*key) == val


if __name__ == '__main__':
    test()