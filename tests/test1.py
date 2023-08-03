import pytest


@pytest.fixture()
def set_up():
    print("Login into system")
    yield
    print("Logout from system")


def test_sending_mail_1(set_up):
    print("Sending an email")


def test_sending_mail_2(set_up):
    print("Sending an email")