from .search_page import SearchPage
from .selectors import Search
from selenium.webdriver.common.keys import Keys as key

# сценарий 1
def test_search(browser):
    url = "https://yandex.ru"
    need_link = "https://tensor.ru/"
    # открываем главню страницу
    page = SearchPage(browser, url)
    page.open()
    # вводим тензор
    elem = page.find_element(Search.text_input)
    page.input_text(elem, "тензор")
    # проверка появления окна suggest
    if not page.exist_element(Search.wait_sugest):
        raise Exception("suggest is not opened")
    # перехо на следующую страницу
    page.input_text(elem, key.ENTER)
    # находим ссылки первых 5 результатов
    elem = page.find_elements(Search.search_result)
    href_list = find_href(elem, 5)
    # проверка существования необходимой ссылки в первых 5
    assert need_link in href_list, f"the links '{need_link}' not in first 5 links (stage 6)"



def find_href(elem, size):
    href_list = []
    for item in elem[0:size]:
        link = item.find_element_by_tag_name("a")
        href = link.get_attribute("href")
        href_list.append(href)
    return href_list
