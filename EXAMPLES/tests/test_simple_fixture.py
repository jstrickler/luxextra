import os
import pytest

from .silly import Silly
    
@pytest.fixture
def silly_object():
    return Silly()  # fixture returns instance of Silly

def test_silly_triples_value(silly_object):  # pass fixture as test parameter
    assert silly_object.triple(5) == 15

def test_silly_normalizes_string(silly_object):
    assert silly_object.normalize("   Spam   ") == "spam"
