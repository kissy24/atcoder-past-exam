import pytest
from ..a import double_num


class Test_double_num:
    @pytest.mark.parametrize("input, expected", [("123", 246), ("012", 24)])
    def test_ReturnsDoubleNum_TakesOnlyNumChars(self, input, expected):
        assert double_num(input) == expected

    @pytest.mark.parametrize("input", ["abc", "0x8"])
    def test_ReturnsValueError_TakesCotainingAlphabetChars(self, input):
        assert isinstance(double_num(input), ValueError)
