import pytest

class UnhappyPath:

    def all_good_and_dandy(self):
        return "It's all good man"

    def when_things_go_wrong(self):
        raise Exception("Not good at all, man!")


def test_if_it_is_all_good():
    target = UnhappyPath()
    assert target.all_good_and_dandy() == "It's all good man"


def test_if_we_have_a_problem():
    target = UnhappyPath()
    with pytest.raises(Exception):
        target.when_things_go_wrong()
