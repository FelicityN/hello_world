"""Tests the mathematical functions defined in demo2.py
"""

import pytest

def test_square():
    """Tests the squaring function"""

    from demo.demo2 import square

    assert 4 == square(2)
