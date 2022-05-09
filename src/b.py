from dataclasses import dataclass, InitVar
from typing import ClassVar, Iterable


@dataclass
class GradedSequence:
    """階差数列を生成するクラス"""

    GREATER: ClassVar[str] = "up"
    LESS: ClassVar[str] = "down"
    EQUAL: ClassVar[str] = "stay"
    sequence: InitVar[list[int]]

    def __post_init__(self, sequence: list[int]):
        if len(sequence) < 2:
            raise ValueError("sequence must have at least 2 elements")
        else:
            self.graded_sequence = list(
                map(lambda x, y: x - y, sequence[1:], sequence[:-1])
            )

    def format(self) -> list[str]:
        """階差数列を出力用フォーマットに変換する

        Returns:
            list[str]: 出力用フォーマット
        """

        def _format(num: int) -> str:
            if num > 0:
                return f"{self.GREATER} {num}"
            if num < 0:
                return f"{self.LESS} {abs(num)}"
            return self.EQUAL

        return list(map(_format, self.graded_sequence))


def print_(iter_: Iterable) -> None:
    for elm in iter_:
        print(elm)


def main():
    sales_duration = int(input())
    sales = [int(input()) for _ in range(sales_duration)]
    sales_diffs: list[str] = GradedSequence(sales).format()
    print_(sales_diffs)


if __name__ == "__main__":
    main()
