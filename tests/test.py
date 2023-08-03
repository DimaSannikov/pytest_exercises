import pytest


@pytest.fixture()
def set_up():
    print("Before test")
    yield
    print("After test")

def test_equal(set_up):
    assert 1 == 1, "Number is not equal to expected"

def test_is_not_equal(set_up):
    assert 1 != 2, "Number is equal"