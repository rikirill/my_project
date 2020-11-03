from selenium.webdriver.common.by import By

# селекторы для первого сценария
class Search:
    text_input = [By.CSS_SELECTOR, "#text"]
    wait_sugest = [By.XPATH, "/html/body/div[7]"]
    search_result = [By.CSS_SELECTOR, "#search-result > li"]

# для второго
class Image:
    image_link = [By.CSS_SELECTOR, "[data-id='images']"]
    first_category = [By.CSS_SELECTOR, ".PopularRequestList :first-child > [class*=SearchText]"]
    first_image = [By.CSS_SELECTOR, ".serp-controller__content div:first-child > a"]
    next_button = [By.CSS_SELECTOR, "[class*=ButtonNext]"]
    back_button = [By.CSS_SELECTOR, "[class*=ButtonPrev]"]