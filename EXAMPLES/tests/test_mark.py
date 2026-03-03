import pytest

@pytest.mark.alpha  # Mark with label alpha
def test_one():
    assert 1

@pytest.mark.beta
@pytest.mark.alpha  # Mark with label alpha
def test_two():
    assert 1

@pytest.mark.gamma
@pytest.mark.beta  # Mark with label beta
def test_three():
    assert 1

