from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# реализация page object
class PageClass:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 30)
    # открытие главной страницы
    def open(self):
        self.browser.get(self.url)

    # нахождение элемента
    def find_element(self, arg):
        return self.browser.find_element(arg[0], arg[1])

    # нахождение элементов
    def find_elements(self, arg):
        return self.browser.find_elements(arg[0], arg[1])

    # проверка существования элементов
    def exist_element(self, arg):
        try:
            self.wait.until(EC.element_to_be_clickable((arg[0], arg[1])))
        except:
            return False
        return True

