import pytest
from ..e import User, Users, SNS


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
        users = Users(3)
        assert users == [User(i) for i in range(3)]
        assert str(users) == "NNN\nNNN\nNNN"
        assert users.__len__() == 3


class Test_SNS:
    @pytest.fixture
    def sns(self) -> SNS:
        return SNS(3, [[1, 1, 2], [1, 2, 3], [2, 3], [3, 1]])

    class Test_restore:
        def test_restore(self, sns: SNS):
            assert str(sns.restore()) == "NYY\nNNY\nNYN"

    class Test_follow:
        def test_follow(self, sns: SNS):
            sns.follow(1, 2)
            assert sns.users[1].following == [2]
            assert sns.users[2].follower == [1]

    class Test_follow_back:
        def test_follow_back(self, sns: SNS):
            sns.users[1].follower = [2]
            sns.users[2].following = [1]
            sns.follow_back(1)
            assert sns.users[1].following == [2]
            assert sns.users[2].follower == [1]

    class Test_follow_follow:
        def test_follow_follow(self, sns: SNS):
            sns.users[0].following = [1]
            sns.users[1].follower = [0]
            sns.users[1].following = [2]
            sns.users[2].follower = [1]
            sns.follow_follow(0)
            assert sns.users[0].following == [1, 2]
            assert sns.users[2].follower == [1, 0]
