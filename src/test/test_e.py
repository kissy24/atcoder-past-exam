import pytest
from ..e import User, Users, SNS, parse


@pytest.fixture
def user_one() -> User:
    user_one = User(1)
    user_one.follow(4)
    user_one.followed(5)
    return user_one


class Test_User:
    class Test_follow:
        def test_followIt_notHaveFollowingUser(self, user_one: User):
            user_one.follow(2)
            assert sorted(user_one.following) == [2, 4]

        def test_notFollowIt_HasFollowingUser(self, user_one: User):
            user_one.follow(4)
            assert user_one.following == [4]

        def test_notFollowIt_followOwn(self, user_one: User):
            user_one.follow(1)
            assert user_one.following == [4]

    class Test_followed:
        def test_followedIt_notHaveFollowedUser(self, user_one: User):
            user_one.followed(3)
            assert sorted(user_one.follower) == [3, 5]

        def test_notFollowedIt_HasFollowedUser(self, user_one: User):
            user_one.follow(5)
            assert user_one.follower == [5]

        def test_notFollowIt_followOwn(self, user_one: User):
            user_one.follow(1)
            assert user_one.follower == [5]

    class Test_is_following:
        def test_is_following(self, user_one: User):
            assert user_one.is_following(4)


class Test_Users:
    def test_init(self):
        ...


class Test_SNS:
    class Test_restore:
        ...

    class Test_follow:
        ...

    class Test_follow_back:
        ...

    class Test_follow_follow:
        ...


class Test_parse:
    def test_parse(self):
        ...
