"""
Задача:
Создайте функцию, которая принимает в качестве параметров список целых
чисел и длину группы. Ваша задача — определить, можно ли разбить все
числа из списка на группы заданной длины, убедившись при этом, что в
каждой группе присутствуют последовательные числа.

Вход:
lst: Список целых чисел, представляющих числа, которые нужно разделить
на группы.

group_len: Целое число, указывающее желаемую длину каждой группы.
Выход:

Функция должна вернуть True, если возможно создавать группы по критериям,
и False в противном случае. 
"""

from collections import Counter


def consecutive_nums(lst: list, n: int) -> bool:
    """
    Определяет можно ли разбить список целых чисел на группы по N элементов,
    которые являются последовательностью, так что бы были задействованы все
    элементы исходного списка.
    """
    if not len(lst) % n:
        arr, out = dict(sorted(Counter(lst).items(), key=lambda x: x[0])), []
        for _ in range(len(lst) // n):
            out.append(list(arr)[:n])
            for x in out[-1]:
                arr[x] -= 1
                if not arr[x]:
                    del arr[x]
        if len(set().union(*[{v - x[i-1] for i, v in enumerate(x) if i} for x in out])) < 2:
            return True
    return False


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 3, 5], 1), True),
        (([5, 6, 3, 4], 2), True),
        (([1, 3, 4, 5], 2), False),
        (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True),
        (([1, 2, 3, 4, 5], 4), False),
        (([6, 6, 6, 9, 7, 8, 7, 5, 8, 5, 7, 8], 4), True),
        (([3, 9, 2, 2, 7, 6, 5, 8, 5, 2, 7, 4, 5, 3, 4, 4, 6, 2, 3, 4], 4), False),
        (([3, 4, 1, 2, 3, 2, 3, 4, 5], 3), True),
        (([9, 9, 7, 3, 3, 1, 1, 1, 2, 8, 8, 7, 2, 2, 3], 3), True),
        (([5, 5, 7, 3, 3, 1, 1, 1, 2, 6, 6, 7, 2, 2, 3], 3), True),
    )
    for key, val in data:
        assert consecutive_nums(*key) == val


if __name__ == '__main__':
    test()