import sourcecode
import pytest

def test_ceaser():
    assert sourcecode.ceaser('a', 1, False) == 'b'
    assert sourcecode.ceaser('a', 1, True) == 'z'
    assert sourcecode.ceaser('A', 1, False) == 'B'
    assert sourcecode.ceaser('A', 1, True) == 'Z'
    assert sourcecode.ceaser('ABC ABC', 1, False) == 'BCD BCD'
    assert sourcecode.ceaser('XYZ XYZ', 1, False) == 'YZA YZA'
    assert sourcecode.ceaser('xyz xyz', 1, True) == 'wxy wxy'