def pick_third_largest_num(sequence: list[int]) -> int:
    """数列から3番目に大きい整数を取得する
    Args:
        sequence (list): 整数のリスト
    Returns:
        (int): 3番目に大きい整数
    """
    return sorted(sequence)[-3]


def main():
    seq = list(map(int, input().split()))
    print(pick_third_largest_num(seq))


if __name__ == "__main__":
    main()
