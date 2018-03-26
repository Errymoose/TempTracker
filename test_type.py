from TempTracker import TempTracker, TypeException
import pytest

def test_answer():
    tt = TempTracker()

    tt.insert(0)
    tt.insert(55)
    tt.insert(110)

    with pytest.raises(TypeException):
        tt.insert('100')

    with pytest.raises(TypeException):
        tt.insert(100.0)

    with pytest.raises(TypeException):
        tt.insert([100])

