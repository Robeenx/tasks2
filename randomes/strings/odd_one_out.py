"""
Завершите функцию, которая принимает строку в качестве входных данных и
возвращает список всех непарных символов (т. е. они встречаются в строке
нечетное количество раз) в том порядке, в котором они встречались в виде
массива.

В случае выбора из нескольких появлений выберите последнее вхождение непарного
символа.

Примечания:

    Используется широкий спектр символов, и некоторые из них могут неправильно
    отображаться в вашем браузере.
    Ваше решение должно быть линейным с точки зрения длины строки, чтобы
    пройти последний тест.

Примеры

"Hello World"   -->  ["H", "e", " ", "W", "r", "l", "d"]
"Codewars"      -->  ["C", "o", "d", "e", "w", "a", "r", "s"]
"woowee"        -->  []
"wwoooowweeee"  -->  []
"racecar"       -->  ["e"]
"Mamma"         -->  ["M"]
"Mama"          -->  ["M", "m"]
"""


from collections import Counter


def odd_one_out(s: str) -> list[str]:
    """
    Поиск в строке всех не парных символов,
    сортировка по нахождению в строке, вывод последней встречающейся.
    """
    return sorted([x for x, i in Counter(s).items() if i % 2], key=s.rfind)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('Hello World', ["H", "e", " ", "W", "r", "l", "d"]),
        ('Codewars', ["C", "o", "d", "e", "w", "a", "r", "s"]),
        ('woowee', []),
        ('wwoooowweeee', []),
        ('racecar', ["e"]),
        ('Mamma', ["M"]),
        ('Mama', ["M", "m"]),
        ('¼ x 4 = 1', ["¼", "x", "4", "=", "1"]),
        ('¼ x 4 = 1 and ½ x 4 = 2', ["¼", "1", "a", "n", "d", "½", "2"]),
    )
    for key, val in data:
        assert odd_one_out(key) == val


if __name__ == '__main__':
    test()