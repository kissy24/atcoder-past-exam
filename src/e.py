from dataclasses import dataclass, field, InitVar


@dataclass(frozen=True)
class User:
    id: int
    following: list[int] = field(init=False, default_factory=list)
    follower: list[int] = field(init=False, default_factory=list)

    def follow(self, tgt_id: int) -> None:
        """フォローする

        Args:
            tgt_id (int): 対象となるユーザID
        """
        if tgt_id != self.id and tgt_id not in self.following:
            self.following.append(tgt_id)

    def followed(self, tgt_id: int) -> None:
        """フォローされる

        Args:
            tgt_id (int): 対象となるユーザID
        """
        if tgt_id != self.id and tgt_id not in self.follower:
            self.follower.append(tgt_id)

    def is_following(self, tgt_id: int) -> bool:
        """フォローしているかどうか

        Args:
            tgt_id (int): 対象となるユーザID
        """
        return tgt_id in self.following


class Users(list[User]):
    FMT = {
        True: "Y",
        False: "N",
    }

    def __init__(self, obj=()):
        if isinstance(obj, int):
            self.extend(User(i) for i in range(obj))
        else:
            super().__init__(obj)

    def __str__(self):
        return "\n".join(
            "".join(self.FMT[usr.is_following(id_)] for id_ in range(len(self)))
            for usr in self
        )


@dataclass
class SNS:
    user_cnt: InitVar[int]
    logs: list[list[int]]
    users: Users = field(init=False, default_factory=Users)

    def __post_init__(self, user_cnt):
        self.users.__init__(user_cnt)

    @property
    def methods(self):
        return {
            1: self.follow,
            2: self.follow_back,
            3: self.follow_follow,
        }

    def restore(self) -> Users:
        """ログを元にユーザー情報を復元する"""
        for log in self.logs:
            method, *args = log
            self.methods[method](*(arg - 1 for arg in args))
        return self.users

    def follow(self, user: int, target: int) -> None:
        """ユーザーが対象のユーザーをフォローする"""
        self.users[user].follow(target)
        self.users[target].followed(user)

    def follow_back(self, user: int) -> None:
        """ユーザーがフォローバックする"""
        for f in self.users[user].follower:
            self.follow(user, f)

    def follow_follow(self, user: int) -> None:
        """ユーザーがフォローフォローする"""
        ffs = [self.users[f].following for f in self.users[user].following]
        for ff in sum(ffs, []):
            self.follow(user, ff)


def parse() -> tuple[int, int, list[list[int]]]:
    """標準入力を解析する

    Returns:
        tuple[int, int, list[list[int]]]: ユーザーの総数, 操作ログの行数, 操作ログの内容
    """

    def ints(inp: str):
        return [int(i) for i in inp.split()]

    user_cnt, log_cnt = ints(input())
    logs = [ints(input()) for _ in range(log_cnt)]
    return user_cnt, log_cnt, logs


def main():
    user_cnt, _, logs = parse()
    print(SNS(user_cnt, logs).restore())


if __name__ == "__main__":
    main()
