import pytest
from base.capsfactory import CapsFactory


# Conftest should always be on the same level in the dir as the test file(s)

@pytest.fixture()
def setUp():
    print("Running method level set up")
    yield
    print("Running method level tear down")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, device):
    print("Running one time setup")
    caps = CapsFactory(device)
    driver = caps.getDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tear down")


def pytest_addoption(parser):
    parser.addoption("--device", help="ios-sim || android-sim || physical_android_caps || physical_ios_caps")
    parser.addoption("--osVersion")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.fixture(scope="session")
def osVersion(request):
    return request.config.getoption("--osVersion")
