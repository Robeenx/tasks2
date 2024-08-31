"""
 Возвращает номер банковского счета, полученный из указанной строки.

Вы работаете в банке, который недавно приобрел гениальную машину для чтения
писем и факсов, присылаемых из филиалов.
Аппарат сканирует бумажные документы и выдает строку с банковским счетом,
которая выглядит следующим образом:

 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|

Каждая строка содержит номер счета, записанный с использованием символов
вертикальной черты и подчеркивания.
Каждый номер счета должен содержать хотя бы одну цифру, каждая из которых
должна находиться в диапазоне от 0 до 9.

Ваша задача — написать функцию, которая может брать строку банковского счета и
анализировать ее в фактические номера счетов.

 @param {string} bankAccount
 @return {number}

Примеры:


   '    _  _     _  _  _  _  _ \n'+
   '  | _| _||_||_ |_   ||_||_|\n'+     => 123456789
   '  ||_  _|  | _||_|  ||_| _|\n'

   ' _  _  _  _  _  _  _  _  _ \n'+
   '| | _| _|| ||_ |_   ||_||_|\n'+     => 23056789
   '|_||_  _||_| _||_|  ||_| _|\n',

   ' _  _  _  _  _  _  _  _  _ \n'+
   '|_| _| _||_||_ |_ |_||_||_|\n'+     => 823856989
   '|_||_  _||_| _||_| _||_| _|\n',

"""


def parse_bank_account(s: str) -> int:
    """
    Из переданной строки парсит номер.
    """
    w =\
    ' _     _  _     _  _  _  _  _ \n'+\
    '| |  | _| _||_||_ |_   ||_||_|\n'+\
    '|_|  ||_  _|  | _||_|  ||_| _|\n'
    w, s = [list(zip(*x.split('\n')[:-1])) for x in (w, s)]
    w, s = [[(tuple(x[i*3:i*3+3]), str(n)) for n, i in enumerate(range(len(x) // 3))] for x in (w, s)]
    return int(''.join([dict(w)[x[0]] for x in s]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            '    _  _     _  _  _  _  _ \n'+
            ('  | _| _||_||_ |_   ||_||_|\n'+
            '  ||_  _|  | _||_|  ||_| _|\n'),
            123456789
        ),
        (
            (' _  _  _  _  _  _  _  _  _ \n'+
            '| | _| _|| ||_ |_   ||_||_|\n'+
            '|_||_  _||_| _||_|  ||_| _|\n'),
            23056789,
        ),
        (
            (' _  _  _  _  _  _  _  _  _ \n'+
            '|_| _| _||_||_ |_ |_||_||_|\n'+ 
            '|_||_  _||_| _||_| _||_| _|\n'),
            823856989
        )
    )
    for key, val in data:
        assert parse_bank_account(key) == val


if __name__ == '__main__':
    test()
