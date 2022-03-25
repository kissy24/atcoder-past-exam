from typing import Union


def double_num(chars: str) -> Union[int, Exception]:
    """文字列が数値であれば2倍する
    Args:
        chars(str): 文字列
    Returns:
        (int | Exception): 2倍された数値 | 数値以外の文字の場合は、errorを返す
    """
    return int(chars) * 2 if chars.isdecimal() else ValueError("error")


def main():
    print(double_num(input()))


if __name__ == "__main__":
    main()
