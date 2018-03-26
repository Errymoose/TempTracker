from TempTracker import TempTracker, TypeException
import pytest

def test_answer():
    tt = TempTracker()

    tt.insert(109)
    assert tt.get_mean() == 109.0
    
    tt.insert(110)
    assert tt.get_mean() == 109.5

    tt.insert(0)
    assert tt.get_mean() == 73.0

    tt.insert(0)
    assert tt.get_mean() == 54.75

    tt.insert(56)
    assert tt.get_mean() == 55

    tt.insert(0)
    assert tt.get_mean() - 0.0001 <= 45.83333333333 <= tt.get_mean() + 0.0001



