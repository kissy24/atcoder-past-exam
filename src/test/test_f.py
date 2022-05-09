import pytest
from ..f import sort_by_double_camel


class Test_sort_by_double_camel:
    @pytest.mark.parametrize(
        "chars, expected",
        [
            ("FisHDoGCaTAAAaAAbCAC", "AAAaAAbCACCaTDoGFisH"),
            ("AAAAAjhfgaBCsahdfakGZsZGdEAA", "AAAAAAAjhfgaBCsahdfakGGdEZsZ"),
        ],
    )
    def test_returnsSortedDoubleCamels(self, chars, expected):
        assert sort_by_double_camel(chars) == expected
