def test_one(silly_object):   # unit test that uses fixture from conftest.py
    assert silly_object.triple(5) == 15
    assert silly_object.normalize("   Spam   ") == "spam"
