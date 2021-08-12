import pytest
from unittest.mock import MagicMock
from unittest.mock import Mock


class Dependency:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Base:
    def __init__(self, dependency):
        self.dependency = dependency

    def get_dependency_value(self):
        return self.dependency.get_value()


def test_mock_object():
    dep = Mock(spec=Dependency)

    dep.get_value.return_value = 42

    base = Base(dep)

    assert base.get_dependency_value() == 42