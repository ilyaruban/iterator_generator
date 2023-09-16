class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.start_counter = -1

    def __iter__(self):
        self.start_counter = self.start_counter + 1
        self.nested_counter = 0
        return self

    def __next__(self):
        if self.nested_counter == len(self.list_of_list[self.start_counter]):
            iter(self)
        if self.start_counter == len(self.list_of_list):
            raise StopIteration
        self.nested_counter = self.nested_counter + 1
        return self.list_of_list[self.start_counter][self.nested_counter - 1]

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