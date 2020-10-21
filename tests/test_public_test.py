from public_test import __version__, ANSWER


def test_version():
    assert __version__ == '0.1.0'


def test_answer():
    assert ANSWER == 42
