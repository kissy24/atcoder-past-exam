from typing import Final
import pytest
from ..b import GradedSequence


class Test_GradedSequence:
    class Test_format:
        seq: Final[list[int]] = [9, 10, 3, 100, 100, 90, 80, 10, 30, 10]
        expected: Final[list[str]] = [
            "up 1",
            "down 7",
            "up 97",
            "stay",
            "down 10",
            "down 10",
            "down 70",
            "up 20",
            "down 20",
        ]

        @pytest.fixture
        def graded_sequence(self) -> GradedSequence:
            return GradedSequence(self.seq)

        def test_returnsGradedSequenceWithPrefix_takesGradedSequence(
            self, graded_sequence: GradedSequence
        ):
            assert graded_sequence.format() == self.expected
