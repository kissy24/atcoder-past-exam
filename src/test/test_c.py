import pytest
from ..c import PickThirdLargestNumber


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([4, 18, 25, 20, 9, 13], 18),
        ([95, 96, 97, 98, 99, 100], 98),
        ([19, 92, 3, 35, 78, 1], 35),
    ],
)
class Test_PickThirdLargestNumber:
    def test_ReturnsThirdLargestNumber_TakesSequence(self, sequence, expected):
        assert PickThirdLargestNumber(sequence) == expected
