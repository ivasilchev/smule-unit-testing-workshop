import pytest

class Example:
    def the_answer_to_life_universe_and_everything(self):
        return 42

def test_if_the_answer_is_correct():
    example = Example()
    assert example.the_answer_to_life_universe_and_everything() == 42
