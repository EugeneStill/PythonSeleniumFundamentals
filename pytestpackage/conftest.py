import pytest

# setUp runs before each method
# oneTimeSetUp below only runs once at the beginning of the module/class and end of module/class
# oneTimeSetUp only runs at the module level, because we are using scope="module"
# When we use the set up methods as parameters in our calling methods, be sure to call them in the order we want to run
# EG. oneTimeSetUp should be before setUp

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

# We can use the command line option fixtures in our other methods
# Scope could be class, module or session.  Other values might also be valid
@pytest.yield_fixture(scope="class")
# Pass request in as well as specific parameters like browser so that we can access fields like value
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")
    # If request instancs is not None then set the class attribute to value.  This class attribute is available to all
    # test methods
    if request.cls is not None:
        request.cls.value = value
    # yield will return the value to where this fixture is called, the test class demo
    yield value
    print("Running one time tearDown")

# Use parser to add options that can be accepted from the command line
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

# Use methods below to return options from the command line request
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")