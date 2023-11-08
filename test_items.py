import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket(browser):
   #Тест проверяет, что страница товара содержит кнопку добавления в корзину

    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Кнопка найдена"


