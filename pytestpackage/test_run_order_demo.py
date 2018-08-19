"""
SEE DOCS
http://pytest-ordering.readthedocs.io/en/develop/
ANIL MENTIONED THAT SOME OF THESE MARKINGS WERE NOT WORKING WHEN HE TRIED THEM
@pytest.mark.order2
def test_foo():
    assert True

@pytest.mark.order1
def test_bar():
    assert True


@pytest.mark.second_to_last
def test_three():
    assert True

@pytest.mark.last
def test_four():
    assert True

@pytest.mark.second
def test_two():
    assert True

@pytest.mark.first
def test_one():
    assert True


@pytest.mark.run(after='test_second')
def test_third():
    assert True

def test_second():
    assert True

@pytest.mark.run(before='test_second')
def test_first():
    assert True
"""

import pytest

# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(oneTimeSetUp, setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print("Running method E")

@pytest.mark.run(order=6)
def test_run_order_methodF(oneTimeSetUp, setUp):
    print("Running method F")

