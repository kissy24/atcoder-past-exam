from ..d import DuplicateInspection


class Test_DuplicateInspection:
    class Test_inspect:
        def test_returnsDuplicatedPair_thisClassHasDuplicatedSequence(self):
            di = DuplicateInspection([1, 2, 3, 4, 5, 5])
            assert di.inspect() == "5 6"

        def test_returnsCorrect_thisClassHasNonDuplicatedSequence(self):
            di = DuplicateInspection([1, 2, 3, 4, 5, 6])
            assert di.inspect() == "Correct"
