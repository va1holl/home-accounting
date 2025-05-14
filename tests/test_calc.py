import pytest
from test import plus


def test_test():
    assert plus(1, 1) == 2
    assert plus(2, 5) == 7
    assert plus(2, -1) == 1
    assert plus(2, -10) == -8