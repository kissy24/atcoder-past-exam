from typing import NamedTuple, Union
from collections import Counter


class Message(NamedTuple):
    """出力メッセージ"""

    missing = "{dup} {miss}"
    not_missing = "Correct"


def find_dup_and_miss_num(seq: list[int]) -> Union[tuple[int, int], tuple[None, None]]:
    """数列から重複値と欠損値を探す

    Args:
        seq (list[int]): 数列

    Returns:
        Union[tuple[int, int], tuple[None, None]]: 重複値と欠損値 | 重複と欠損がない場合
    """
    counter = Counter({n: 0 for n in range(1, len(seq) + 1)})
    counter.update(seq)
    if all(counter.values()):
        return None, None
    counts = counter.most_common()
    return counts[0][0], counts[-1][0]


def main():
    len_ = int(input())
    seq = [int(input()) for _ in range(len_)]
    dup, miss = find_dup_and_miss_num(seq)
    msg = Message.not_missing if miss is None else Message.missing
    print(msg.format(dup=dup, miss=miss))


if __name__ == "__main__":
    main()
