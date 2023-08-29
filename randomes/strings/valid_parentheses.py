"""
Напишите функцию, которая принимает строку круглых скобок и определяет,
допустим ли порядок круглых скобок. Функция должна вернуть trueесли
строка действительна, и falseесли он недействителен.

Примеры:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Ограничения:
0 <= length of input <= 100

Все входные данные будут строками, состоящими только из символов. (и ).
Пустые строки считаются сбалансированными (и, следовательно, действительными)
и будут проверены.
"""


def valid_parentheses(paren_str: str) -> bool:
    """
    Проверяет наличие в строке всех парных скобок.
    """
    tmp = 0
    for x in paren_str:
        tmp += {'(': 1, ')': -1}.get(x, 0)
        if tmp < 0:
            break
    return not tmp


def test() -> None:
    """Тестирование работы алгоритмов."""

    data1 = (
        "()",
        "((()))",
        "()()()",
        "(()())()",
        "()(())((()))(())()",
    )

    data2 = (
        ")(",
        "()()(",
        "((())",
        "())(()",
        ")()",
        ")",
    )

    for key in data1:
        assert valid_parentheses(key)

    for key in data2:
        assert not valid_parentheses(key)


if __name__ == '__main__':
    test()
