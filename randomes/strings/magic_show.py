"""
Телепатия:

Это простой магический трюк.

Я нахожу это захватывающим после просмотра этого волшебного трюка.

Вот как проходит трюк:

Во-первых, у фокусника на руках 6 карт.

Затем фокусник просит вас выбрать число от 0 до 60 и запомнить его.

После этого фокусник скажет вам сказать «Да», когда вы увидите среди карт
выбранное вами число, в противном случае скажите «Нет».

Наконец, маг, выслушав все ваши ответы, сможет почувствовать число, которое вы
запомнили, и раскрыть его.

Задача:

Ваша задача – сыграть роль волшебника.

Я дам вам строку, представляющую ответы аудитории.

Вам нужно угадать число, выбранное зрителями.

На карточке написано несколько чисел, и этот набор из 6 карточек никогда не
меняется.

"| Card 1: Yes | Card 2: Yes | Card 3: Yes | Card 4: Yes | Card 5: No | Card 6: Yes |" -> 47

Only 1 line of code and 106 characters of code can be used.

Мы приветствуем всех приверженцев кода, оставляющих комментарии по тем
областям, которые они хотели бы улучшить или сохранить.
"""


def magic_show(s: str) -> int:
    """
    Угадывает число записанное на карточках.
    """
    return int(''.join([{'Y': '1', 'N': '0'}.get(x, '') for x in s][::-1]), 2)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (47, "| Card 1: Yes | Card 2: Yes | Card 3: Yes | Card 4: Yes | Card 5: No | Card 6: Yes |"),
        (46, "| Card 1: No | Card 2: Yes | Card 3: Yes | Card 4: Yes | Card 5: No | Card 6: Yes |"),
        (55, "| Card 1: Yes | Card 2: Yes | Card 3: Yes | Card 4: No | Card 5: Yes | Card 6: Yes |"),
        (38, "| Card 1: No | Card 2: Yes | Card 3: Yes | Card 4: No | Card 5: No | Card 6: Yes |")
    )
    for val, key in data:
        assert magic_show(key) == val


if __name__ == '__main__':
    test()