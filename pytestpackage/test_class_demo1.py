import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    # Use fixture to create an object of SomeClassToTest.
    # Autouse=True makes it available to all methods.
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        # Use class level object in the method
        result = self.abc.sumNumbers(2, 8)
        # Since we are using pytest we can assert directly rather than using assert methods from unittest
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")