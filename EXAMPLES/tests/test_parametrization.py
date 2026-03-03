import pytest
from .silly import Silly
    
@pytest.fixture
def silly_object():
    return Silly()  # fixture returns instance of Silly

# List of values for testing containing input and expected result
test_data = [
    (5, 15), ('a', 'aaa'), (False, False), (True, 3), (0, 0), ([True], [True, True, True])
]  

# Parametrize the test with the test data; the first argument is a string mapping 
# parameters to the test data
@pytest.mark.parametrize("input,expected", test_data)  
def test_triple(silly_object, input, expected): 
    assert silly_object.triple(input) == expected   # Test the function with the parameters

