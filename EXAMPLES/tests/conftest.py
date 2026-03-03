#!/usr/bin/env python
from pytest import fixture
from .silly import Silly
    
@fixture
def silly_object():
    return Silly()  # fixture returns instance of Silly

# predefined hook (all hooks start with 'pytest_')
def pytest_runtest_setup(item):  # item is test function
    if "test_config" in str(item):
        print(f"Hello from setup, {item}", end=" ")
