"""
Задача

Приближается Рождество, и ваша задача — построить собственную рождественскую
елку с указанными персонажами и заданной высотой.
Входы:

    chars: указанные символы.
    n: указанная высота. Положительное целое число, большее 2.

Выход:

    Многострочная строка. Каждая строка разделена \n. Дерево состоит из двух
    частей: листьев и ствола.

Листья должны быть n ряды. В первой строке введите 1 символ, во второй строке
— 3 символа и так далее. Между двумя корректирующими символами будет добавлен
один пробел, а некоторые необходимые пробелы будут добавлены с левой стороны,
чтобы сохранить форму дерева. Справа места добавлять не нужно.

Ствол должен быть не менее 1 единицы высоты, это зависит от величины n.
Минимальное значение n равно 3, а высота ствола дерева равна 1 единице высоты.
Если n увеличился на 3, а ствол дерева увеличился на 1 единицу. Например, если
n равно 3, 4 или 5, ствол должен состоять из 1 строки; когда n равно 6,7 или 8,
ствол должен быть 2-рядным; и так далее.

Все еще не поняли задачу? Посмотрите на следующий пример ;-)
Примеры

Для chars = "*@o" and n = 3, вывод должен быть:

  *
 @ o
* @ o
  |

Для chars = "*@o" and n = 6, вывод должен быть:

     *
    @ o
   * @ o
  * @ o *
 @ o * @ o
* @ o * @ o
     |
     |

Для chars = "1234" and n = 6, вывод должен быть:

     1
    2 3
   4 1 2
  3 4 1 2
 3 4 1 2 3
4 1 2 3 4 1
     |
     |

Для chars = "123456789" and n = 3, вывод должен быть:

  1
 2 3
4 5 6
  |
"""


from itertools import cycle


def custom_christmas_tree(chars: str, n: int) -> str:
    """
    Рисует рождественсую ель из переданных символов циклически, указанной высоты.
    """
    c, x = cycle(chars), n // 3 * f'\n{"|":>{n}}'
    return '\n'.join([f"{' '.join([next(c) for _ in range(i + 1)]):>{n + i}}" for i in range(n)]) + x


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            ("*@o", 6),
            '     *\n    @ o\n   * @ o\n  * @ o *\n @ o * @ o\n* @ o * @ o\n     |\n     |'
        ),
        (
            ("1234", 6),
            '     1\n    2 3\n   4 1 2\n  3 4 1 2\n 3 4 1 2 3\n4 1 2 3 4 1\n     |\n     |'
        ),
        (
            ("123456789", 3),
            '  1\n 2 3\n4 5 6\n  |'
        )
    )
    for key, val in data:
        assert custom_christmas_tree(*key) == val


if __name__ == '__main__':
    test()
