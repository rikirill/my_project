# страница для теста с каритнками (сценарий 2)
class ImagePage(PageClass):
    # функция переключения вкладок
    def switch(self):
        handle = self.browser.window_handles[1]
        self.browser.close()
        self.browser.switch_to.window(handle)

    # получения названия вкладки
    def title(self):
        return self.browser.title

    # получение url страницы
    def current_url(self):
        return self.browser.current_url
