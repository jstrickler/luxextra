import sys
import pytest

def test_one():  # Normal test -- no skipping or failing
    assert True

# Uncondition skip
@pytest.mark.skip(reason="can not currently test")
def test_two():
    assert True

# Skip this test if current platform is not Windows
@pytest.mark.skipif(
    sys.platform != 'win32', 
    reason="only implemented on Windows"
)
def test_three():
    assert True

@pytest.mark.xfail
def test_four():
    assert False

@pytest.mark.xfail
def test_five():
    assert True
