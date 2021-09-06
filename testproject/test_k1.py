import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
time.sleep(1)

driver.get(URL)

a_input = driver.find_element_by_id("a")
b_input = driver.find_element_by_id("b")
submit_button = driver.find_element_by_id("submit")
result_text = driver.find_element_by_id("result")

test_data = [("", ""), ("2", "3"), ("", "",)]
reference_data = ["", "10", "NaN"]


def clear_and_fill_input(element1, element2, text1, text2):
    element1.clear()  # beviteli mezo torlese
    element2.clear()  # beviteli mezo torlese
    element1.send_keys(text1)  # beiratas a mezobe
    element2.send_keys(text2)  # beiratas a mezobe


def test_empty():
    # helyesen jelenik meg (a: <üres>, b: <üres>, c: <nem látszik>)
    clear_and_fill_input(a_input, b_input, test_data[0][0], test_data[0][1])
    submit_button.click()
    assert result_text.text == reference_data[0]


def test_positive():
    # Számítás helyes, megfelelő bemenettel (a: <2>, b: <3>, c: <10>)
    clear_and_fill_input(a_input, b_input, test_data[1][0], test_data[1][1])
    submit_button.click()
    assert result_text.text == reference_data[1]


def test_half_empty():
    # ures kitoltes (a: <ures>, b: <ures>, c: <NaN>)
    clear_and_fill_input(a_input, b_input, test_data[2][0], test_data[2][1])
    submit_button.click()
    assert result_text.text == reference_data[2]


time.sleep(2)
driver.close()
