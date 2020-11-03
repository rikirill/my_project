from selenium import webdriver
import pytest

# опция запуска на определённом браузере
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome, firefox or opera")
start_msg = "\nstart {} browser for test.."


# фикстура на открытие/закрытие браузера в тестах
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print(start_msg.format(browser_name))
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print(start_msg.format(browser_name))
        browser = webdriver.Firefox()
    elif browser_name == "opera":
        print(start_msg.format(browser_name))
        browser = webdriver.Opera()
    elif browser_name == "edge":
        print(start_msg.format(browser_name))
        browser = webdriver.Edge()
    else:
        print(start_msg.format("firefox"))
        browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.close()