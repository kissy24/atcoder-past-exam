import pytest
from ..a import double_num


class Test_double_num:
    @pytest.mark.parametrize("input, expected", [("123", 246), ("012", 24)])
    def test_returnsDoubleNum_takesOnlyNumChars(self, input, expected):
        assert double_num(input) == expected

    @pytest.mark.parametrize("input", ["abc", "0x8"])
    def test_returnsValueError_takesCotainingAlphabetChars(self, input):
        assert isinstance(double_num(input), ValueError)
