from app import get_message, login


def test_get_message():
    assert get_message() == "Hello from DevOps"


def test_login():
    assert login("Saket") == "Welcome, Saket!"


def test_login_rejects_empty_username():
    try:
        login("")
    except ValueError as error:
        assert str(error) == "Username is required"
    else:
        assert False, "Expected ValueError"
