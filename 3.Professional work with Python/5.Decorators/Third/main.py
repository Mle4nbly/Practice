import types
import os
from datetime import datetime

##Приложение generator. Тема:'4.Iterators, generators'

def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open(os.path.join(os.path.dirname(__file__),'main.log'), 'a', encoding='utf8') as log_file:
            log_file.write(f'{datetime.now()}, {old_function.__name__}, {args}|{kwargs}, {result.__name__}\n')
        return result

    return new_function

path = f'{os.path.dirname(__file__)}\\main.log'
if os.path.exists(path):
    os.remove(path)

@logger
def flat_generator(list_of_lists):
    nested_list_cursor = -1
    main_list_cursor = 0
    while main_list_cursor < len(list_of_lists):
        nested_list_cursor += 1
        if nested_list_cursor == len(list_of_lists[main_list_cursor]):
            nested_list_cursor = 0
            main_list_cursor += 1
        if main_list_cursor < len(list_of_lists):
            yield list_of_lists[main_list_cursor][nested_list_cursor]
    
def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()