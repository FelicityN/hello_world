import pytest

def test_square():
    from demo.demo import square
    assert square(6) == 36
