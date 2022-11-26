from collections import Counter
from dataclasses import dataclass, InitVar
from typing import Iterable


@dataclass
class DuplicateInspection(Counter):
    sequence: InitVar[Iterable]

    def __post_init__(self, sequence):
        super().__init__(dict.fromkeys(range(1, len(sequence) + 1), 0))
        self.update(sequence)

    def inspect(self) -> str:
        """重複を検査する

        Returns:
            str: 検査の結果
        """
        dup_num, dup_cnt = self.most_common()[0]
        miss_num, miss_cnt = self.most_common()[-1]
        return "Correct" if dup_cnt == miss_cnt else f"{dup_num} {miss_num}"


def main():
    length = int(input())
    seq = [int(input()) for _ in range(length)]
    print(DuplicateInspection(seq).inspect())


if __name__ == "__main__":
    main()
