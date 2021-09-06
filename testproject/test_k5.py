import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html "
time.sleep(1)
driver.get(URL)

test_data = [25, 75]
list_numbers = driver.find_elements_by_xpath('//*[@id="numbers-list"]/li')
list_cells = driver.find_elements_by_xpath('//td')
play_button = driver.find_element_by_id('spin')
init_button = driver.find_element_by_id('init')


def test_basic_line_up():
    # TC1: Az applikáció helyesen megjelenik:
    # A bingo tábla 25 darab cellát tartalmaz
    # A számlista 75 számot tartalmaz

    print(len(list_numbers))
    print(len(list_cells))
    assert len(list_numbers) == test_data[1]
    assert len(list_cells) == test_data[0]


def test_init_button():
    # TC3: Új játékot tudunk indítani
    # az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    # új bingo szelvényt kapunk más számokkal.
    for i in range(5):
        play_button.click()
    time.sleep(2)
    assert len(driver.find_elements_by_xpath('//li[@class="checked"]')) == 5
    init_button.click()
    time.sleep(2)
    assert len(driver.find_elements_by_xpath('//li[@class="checked"]')) == 0


driver.close()
