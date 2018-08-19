# To run file from CLI: py.test -v -s test_case_demo2.py

import pytest

# Using yield we can put the set up and tear down steps all in one setUp method
# Any code before the yield keyword will run as part of set up
# Any code after the yield keyword will run as part of tear down

@pytest.fixture()
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")