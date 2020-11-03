from .image_page import ImagePage
from .selectors import Image
import time

# сценарий 2
def test_image(browser):
    # открываем главную страницу
    url = "https://yandex.ru"
    page = ImagePage(browser, url)
    page.open()

    # находим ссылку на раздел каритнки и переходим по ней
    page.find_element(Image.image_link).click()
    time.sleep(5)
    page.switch()
    # проверка перехода на нужную страницу
    assert 'https://yandex.ru/images/' in str(page.current_url()), f"the url '{page.current_url()}' is unvaild"
    # переходим на первую категорию
    elem = page.find_element(Image.first_category)
    text = elem.text
    elem.click()
    page.exist_element(Image.first_image)
    # проверяем что перешли на первую
    assert text in  page.title()
    # переходим на первую картинку
    href = page.current_url()
    time.sleep(5)
    page.find_element(Image.first_image).click()
    img_href = page.current_url()
    # проверяем, что перешли на первую картинку
    assert img_href != href, "the opened image doesn't math the one"
    # переходим на картинку вперёд
    page.find_element(Image.next_button).click()
    time.sleep(5)
    # проверяем переход
    assert img_href != page.current_url(), "the next image is the same"
    # переходим назад
    page.find_element(Image.back_button).click()
    time.sleep(5)
    # проверяем переход назад
    assert page.current_url() == img_href, "the previous image is not what it was"


