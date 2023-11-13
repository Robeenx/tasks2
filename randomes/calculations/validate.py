"""
В этом ката вы реализуете алгоритм Луна , который используется для проверки номеров кредитных карт.

Учитывая положительное целое число длиной до 16 цифр, верните trueесли это действительный номер
кредитной карты, и falseесли это не так.

Вот алгоритм:

    Удвойте каждую вторую цифру, сканируя справа налево , начиная со второй цифры (справа).

    Другой способ подумать об этом: если с цифр четное, удвойте каждую вторую цифру, начиная первой;
    если число нечетное цифр , удвойте каждую вторую цифру, начиная со второй :

    1714 ==> [1*, 7, 1*, 4] ==> [2, 7, 2, 4]

    12345 ==> [1, 2*, 3, 4*, 5] ==> [1, 4, 3, 8, 5]

    891 ==> [8, 9*, 1] ==> [8, 18, 1]

    Если полученное число больше 9, замените его суммой собственных цифр
    (что аналогично вычитанию 9 от него):

[8, 18*, 1] ==> [8, (1+8), 1] ==> [8, 9, 1]

or:

[8, 18*, 1] ==> [8, (18-9), 1] ==> [8, 9, 1]

    Суммируем все последние цифры:

    [8, 9, 1] ==> 8 + 9 + 1 = 18

    Наконец, возьмите эту сумму и разделите ее на 10. Если остаток равен нулю, исходный номер
    кредитной карты действителен.

    18 (modulus) 10 ==> 8 , which is not equal to 0, so this is not a valid credit card number
"""


def validate(n: int) -> bool:
    """
    Валидация кредитной карты алгоритмом Луна.
    """
    return not sum(int(x) * [1, 2][i % 2] - [0, 9][i % 2 and 4 < int(x)] for i, x in enumerate(str(n)[::-1])) % 10


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1714, False),
        (12345, False),
        (891, False),
        (123, False),
        (1, False),
        (2121, True),
        (1230, True),
    )
    for key, val in data:
        assert validate(key) == val


if __name__ == '__main__':
    test()
