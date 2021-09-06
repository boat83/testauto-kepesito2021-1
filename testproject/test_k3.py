import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import InvalidSessionIdException

driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
time.sleep(1)
driver.get(URL)

input = driver.find_element_by_id('title')
test_data = [("abcd1234"), ("teszt233@"), ("abcd")]
reference_data = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]
error_msg = driver.find_elements_by_xpath('//span[class="error active"]')


def clear_and_fill_input(element, text):  # megadni: beviteli mezo megkeresve, bekuldendo szoveg
    element.clear()  # beviteli mezo torlese
    element.send_keys(text)  # beiratas a mezobe


def test_positive():
    # TC1 Helyes kitöltés esete: title: abcd1234, Nincs validációs hibazüzenet

    clear_and_fill_input(input, test_data[0])  # input a beviteli mezo megkeresve
    assert len(error_msg) == 0


def test_illegal():
    # TC2 Illegális karakterek esete: title: teszt233@, Only a-z and 0-9 characters allewed.

    clear_and_fill_input(input, test_data[1])  # input a beviteli mezo megkeresve
    time.sleep(2)
    assert driver.find_element_by_xpath('/html/body/form/span').text == reference_data[1]


def test_too_short():
    # TC3 Tul rövid bemenet esete:  title: abcd, Title should be at least 8 characters; you entered 4
    clear_and_fill_input(input, test_data[2])  # input a beviteli mezo megkeresve
    time.sleep(2)
    assert driver.find_element_by_xpath('/html/body/form/span').text == reference_data[2]



driver.close()
