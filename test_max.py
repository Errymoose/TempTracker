from TempTracker import TempTracker, TypeException
import pytest

def test_answer():
    tt = TempTracker()

    tt.insert(0)
    assert tt.get_max() == 0

    tt.insert(55)
    assert tt.get_max() == 55

    tt.insert(11)
    assert tt.get_max() == 55

    tt.insert(56)
    assert tt.get_max() == 56

    tt.insert(55)
    assert tt.get_max() == 56

    tt.insert(110)
    assert tt.get_max() == 110
    
    tt.insert(109)
    assert tt.get_max() == 110


