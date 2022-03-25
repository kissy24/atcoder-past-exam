import re


def sort_by_double_camel(chars: str) -> str:
    """ダブルキャメルケースで分割ソートする
    Args:
        chars(str): ソート対象の文字列
    Returns:
        (list[str]): 昇順でソートされたダブルキャメルケース文字列
    """
    double_camels = sorted(re.findall("[A-Z][a-z]*[A-Z]", chars), key=str.lower)
    return "".join(double_camels)


def main():
    print(sort_by_double_camel(input()))


if __name__ == "__main__":
    main()
