import pytest


@pytest.fixture
def response_body():
    return '{"body": "body contents"}'


class Response:
    def __init__(self, body):
        self.body = body

    def get_body(self):
        return self.body


def test_get_fixturized_body(mocker, response_body):
    mocker.patch.object(Response, 'get_body', return_value=response_body)
    r = Response("test")

    assert r.get_body() != "test"
    assert r.get_body() == '{"body": "body contents"}'