"""
Представьте, что у вас есть список целых чисел.
Вы начинаете с первого пункта и используете каждое значение как ориентир,
чтобы решить, куда идти дальше. Создайте функцию, которая определяет,
образует ли входной список полный цикл или нет.
"""


def full_cycle(lst: list):
    """Проверяет, является ли список полным циклом."""
    return all((x := lst[i and x]) for i in range(len(lst) - 1))


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = (
        ([0, 1], False),
        ([1, 0], True),
        ([2, 1, 0], False),
        ([2, 0, 1], True),
        ([1, 2, 0, 3], False),
        ([3, 2, 0, 1], True),
        ([4, 1, 2, 3, 0], False),
        ([2, 0, 4, 1, 3], True),
        ([1, 3, 4, 0, 5, 2], False),
        ([1, 5, 4, 2, 0, 3], True),
        ([1, 5, 4, 2, 0, 3, 6], False),
        ([6, 8, 3, 0, 2, 7, 4, 1, 5], False),
        ([2, 8, 5, 9, 1, 3, 7, 4, 0, 6], True),
        ([2, 17, 7, 19, 18, 9, 5, 15, 16, 8, 11, 6, 14, 4, 3, 13, 0, 12, 1, 10], True),
        ([21, 18, 19, 14, 8, 0, 9, 2, 1, 3, 7, 4, 5, 10, 13, 12, 6, 17, 11, 15, 20, 16], False),
    )
    for key, val in data:
        assert full_cycle(key) == val


if __name__ == '__main__':
    test()