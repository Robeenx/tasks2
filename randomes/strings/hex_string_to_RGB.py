"""
При работе со значениями цвета иногда может быть полезно извлечь отдельные значения красного,
зеленого и синего (RGB) компонентов цвета. Реализуйте функцию, отвечающую этим требованиям:

    Принимает в качестве параметра шестнадцатеричную цветовую строку без учета регистра
    (например. "#FF9933"или "#ff9933")
    Возвращает Map<String, int> со структурой {r: 255, g: 153, b: 51}где r , g и b находятся в
    диапазоне от 0 до 255

Примечание. Ваша реализация не обязательно должна поддерживать сокращенную форму шестнадцатеричной
записи (т. е. "#FFF")
Пример

"#FF9933" --> {r: 255, g: 153, b: 51}
"""


def hex_string_to_RGB(hex_string: str) -> dict:
    """
    Конвертирует 16-ти ричную строку цвета в RGB.
    """
    return {k: int(f'0x{hex_string[i:i+2].lower()}', 0) for k, i in zip('rgb', range(1, 7, 2))}


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("#FF9933", {'r': 255, 'g': 153, 'b': 51}),
        ("#beaded", {'r': 190, 'g': 173, 'b': 237}),
        ("#000000", {'r': 0, 'g': 0, 'b': 0}),
        ("#111111", {'r': 17, 'g': 17, 'b': 17}),
        ("#Fa3456", {'r': 250, 'g': 52, 'b': 86}),
    )
    for key, val in data:
        assert hex_string_to_RGB(key) == val


if __name__ == '__main__':
    test()