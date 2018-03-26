from TempTracker import TempTracker, RangeException
import pytest
import sys

def test_answer():
    tt = TempTracker()

    tt.insert(0)
    tt.insert(55)
    tt.insert(110)

    with pytest.raises(RangeException):
        tt.insert(111)

    with pytest.raises(RangeException):
        tt.insert(-1)

    with pytest.raises(RangeException):
        tt.insert(sys.maxsize)

