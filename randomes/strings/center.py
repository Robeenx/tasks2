"""
Все строки теперь должны располагаться по центру.
Реализовать функцию, которая принимает строку strng, целое число width,
и необязательный символ fill(по умолчанию: ' ') и возвращает новую
строку длина widthгде strngрасполагается по центру и справа и слева
дополняется fill.

Если левый и правый отступы не могут быть одинаковой длины, сделайте
отступы на левая сторона на один символ длиннее.

Если strng длиннее, чем width, то возвращаться strng без изменений.
"""


def center(strng: str, width: int, fill: str = ' ') -> str:
    """Центрирование строки с помощью заданного символа"""
    return f'{strng:^{width - (len(strng) - width) % 2}}'.rjust(width).replace(' ', fill)


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (("a", 3), " a "),
        (("abcdefg", 2), "abcdefg"),
        (("abc", 10, '_'), "____abc___"),
    )
    for key, val in data:
        assert center(*key) == val


if __name__ == '__main__':
    test()