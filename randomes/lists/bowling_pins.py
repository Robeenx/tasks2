"""
Установите кегли для боулинга!
Задача:

Вы когда-нибудь играли в боулинг? Кратко: вам нужно бросить миску на 10 кеглей,
расположенных следующим образом:

I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1

Вы получите массив целых чисел между 1 и 10, например [3, 5, 9]и должны
удалить их из поля следующим образом:

I I   I
 I   I
  I   
   I   

Возвращает строку с текущим полем.
Обратите внимание, что:

    Строки выводов разделяются новой строкой ( \n)
    Каждая строка должна быть 7 символы длинные
    Заполните недостающие контакты пробелом (  )
"""


def bowling_pins(arr: list[int]) -> str:
    """
    Выставляет кегли, не нарушая строй, учитывая выбывшие.
    """
    return '\n'.join([f"{' '.join([['I', ' '][n in arr] for n in range(x, x + i)]):^7}" for i, x in enumerate((1, 2, 4, 7), 1)][::-1])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([2, 3], "I I I I\n I I I \n       \n   I   "),
        ([1, 2, 10], "I I I  \n I I I \n    I  \n       "),
    )
    for key, val in data:
        assert bowling_pins(key) == val


if __name__ == '__main__':
    test()