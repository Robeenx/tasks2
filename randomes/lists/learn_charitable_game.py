"""
Задача

У вас есть люди, которые делают ставки, и все они начинают с одинаковой суммы денег (это число>0).

Выясните, возможно ли данное конечное состояние сумм после завершения ставок и перераспределения денег.
Ввод, вывод

    [input]целочисленный массив

предлагаемое конечное состояние, показывающее окончательные суммы для каждого игрока

    [output]логическое значение

trueесли это возможное конечное состояние и falseв противном случае
Примеры

    Для arr = [0, 56, 100], вывод должен быть true.

Три игрока начинают с одинаковой суммой денег 52.

В конце игры игрок 1 проигрывает. 52, победа игрока2 4, и игрок3 выигрывает 48.

    Для arr = [0, 0, 0], вывод должен быть false.

Игроки должны начинать с положительного количества денег.

    Для arr = [11], вывод должен быть true.

Один игрок всегда сохраняет свои деньги в конце игры.

    Для arr = [100, 100, 100, 90, 1, 0, 0], вывод должен быть false.

Эти игроки не могут начать с одинаковой суммы денег.

"""


def learn_charitable_game(arr: list) -> bool:
    """
    Проверяет, возможны ли заданные конечные значения игры.
    """
    return any(arr) and (sum(arr) / len(arr)).is_integer()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([100, 100, 100, 90, 1, 0, 0], False),
        ([0, 0, 0, 0], False),
        ([0, 56, 100], True),
        ([33, 19, 38, 87, 93, 4], False),
        ([11], True),
    )
    for key, val in data:
        assert learn_charitable_game(key) == val


if __name__ == '__main__':
    test()