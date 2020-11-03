from .Page import PageClass

# страница для теста с поиском (сценарий 1)
class SearchPage(PageClass):
    # функция ввода текста
    def input_text(self, where, what):
        where.send_keys(what)

