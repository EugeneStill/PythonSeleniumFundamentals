"""
file name should start with test
test method name should start with test

# run tests in module (module is like class):
py.test test_case_demo3.py -v -s

# run all tests below somepath:
If current directory, run all tests this way:
py.test -v -s

# only run a specific test_method in a specific test_module
py.test -v -s test_case_demo3.py::test_demo3_methodA


-s to print statements
-v verbose
"""

import pytest

@pytest.fixture()
def setUp():
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")

def test_demo3_methodB(setUp):
    print("Running demo3 method B")