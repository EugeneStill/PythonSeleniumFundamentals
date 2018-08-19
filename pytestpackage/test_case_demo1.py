import pytest

# Use decorator to classify the method as a fixture
@pytest.fixture()
def setUp():
    print("Running demo1 setUp")

# If we want to use the fixture in other methods, we pass the method name in as a paramater
# If the decorated method is not passed in, then the method below would not call the decorated method
def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")