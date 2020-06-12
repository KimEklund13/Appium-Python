import pytest
from base.capsfactory import CapsFactory


@pytest.fixture()
def create_driver(request, device):
    print("Getting new driver for the test")
    caps_factory = CapsFactory(device)
    driver = caps_factory.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Quitting the driver for this test")


@pytest.fixture()
def get_platform(request, device):
    caps_factory = CapsFactory(device)
    platform = caps_factory.get_platform_name()

    if request.cls is not None:
        request.cls.platform = platform

    yield platform


def pytest_addoption(parser):
    parser.addoption("--device", help="ios-sim || android-sim || android-real-device || ios-real-device")
    parser.addoption("--osVersion")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


# TODO: This currently isn't being used. Will build out args that will be parsed into the CapsFactory
@pytest.fixture(scope="session")
def osVersion(request):
    return request.config.getoption("--osVersion")
