import pytest
from ..c import pick_third_largest_num


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([4, 18, 25, 20, 9, 13], 18),
        ([95, 96, 97, 98, 99, 100], 98),
        ([19, 92, 3, 35, 78, 1], 35),
    ],
)
class Test_pick_third_largest_num:
    def test_returnsThirdLargestNumber_takesSequence(self, sequence, expected):
        assert pick_third_largest_num(sequence) == expected
