class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.item_counter = 0
        self.list_counter = 0
        return self

    def __next__(self):
        if self.list_counter == len(self.list_of_list):
            raise StopIteration
        lists = self.list_of_list[self.list_counter]
        item = lists[self.item_counter]
        self.item_counter += 1
        if self.item_counter == len(lists):
            self.list_counter += 1
            self.item_counter = 0
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()