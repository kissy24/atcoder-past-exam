from ..d import find_dup_and_miss_num


class Test_find_dup_and_miss_num:
    def test_returnsNones_takesSerialNumbers(self):
        assert find_dup_and_miss_num([1, 2, 3, 4, 5, 6]) == (None, None)

    def test_returnsTuple_takesDuplicateNumbers(self):
        assert find_dup_and_miss_num([1, 2, 3, 4, 5, 5]) == (5, 6)
