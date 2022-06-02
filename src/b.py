from dataclasses import dataclass, InitVar
from typing import ClassVar, Iterable


@dataclass
class GradedSequence:
    """階差数列を表現するクラス"""

    GREATER: ClassVar[str] = "up"
    LESS: ClassVar[str] = "down"
    EQUAL: ClassVar[str] = "stay"
    _sequence: InitVar[list[int]]

    def __post_init__(self, _sequence: list[int]):
        if len(_sequence) < 2:
            raise ValueError("sequence must have at least 2 elements")
        else:
            self.graded_sequence = list(
                map(lambda x, y: x - y, _sequence[1:], _sequence[:-1])
            )

    def format(self) -> list[str]:
        """階差数列を出力用にフォーマットする

        Returns:
            list[str]: 増減に合わせてフォーマットされた階差数列
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
