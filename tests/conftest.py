import pytest
from base.capsfactory import CapsFactory


@pytest.fixture()
# Currently not doing anything with the tests. Just here to serve as a method-level fixture example.
def setUp():
    print("Running method level set up -- not doing anything")
    yield
    print("Running method level tear down -- not doing anything")


@pytest.fixture(scope="class")
def one_time_set_up(request, device):
    print("Running one time setup, getting driver")
    caps_factory = CapsFactory(device)
    driver = caps_factory.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tear down")


@pytest.fixture(scope="class")
def get_platform(request, device):
    print("Getting platform for locators")
    caps_factory = CapsFactory(device)
    platform = caps_factory.get_platform_name()

    if request.cls is not None:
        request.cls.platform = platform

    yield platform


def pytest_addoption(parser):
    parser.addoption("--device", help="ios-sim || android-sim || physical_android_caps || physical_ios_caps")
    parser.addoption("--osVersion")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


# TODO: This currently isn't being used. Will build out args that will be parsed into the CapsFactory
@pytest.fixture(scope="session")
def osVersion(request):
    return request.config.getoption("--osVersion")
