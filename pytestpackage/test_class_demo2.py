import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    # since we need to access the value in this class set up, we need to explicitly pass oneTimeSetUp here instead
    # of relying on the mark.usefixtures above.  At least that is what Anil said, but it looks like it works without it too
    # def classSetup(self, oneTimeSetUp):
    def classSetup(self):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")