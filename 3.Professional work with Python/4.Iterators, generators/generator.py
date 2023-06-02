import types


def flat_generator(list_of_lists):
    nested_list_cursor = -1
    main_list_cursor = 0
    while main_list_cursor <= len(list_of_lists)-1:
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