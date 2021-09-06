import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
time.sleep(1)

driver.get(URL)
colors = driver.find_element_by_id('allcolors').text
color_list = colors.replace('"', '').replace(' ', '').split(',')
first_color = driver.find_element_by_id('randomColor')
start_button = driver.find_element_by_id('start')
stop_button = driver.find_element_by_id('stop')
test_data = ['True', 'Correct!', 'Incorrect!']
print(colors)
print(color_list)


def test_buttons():
    # Tc2: El lehet indítani a játékot a start gommbal. Ha elindult a játék akkor a stop gombbal le lehet állítani.
    assert start_button.is_enabled() == True and stop_button.is_enabled() == True



def start_stop():
    # TC3: Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg. ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.
    start_button.click()
    time.sleep(3)
    stop_button.click()
    if driver.find_element_by_id('randomColor').get_attribute('value') == driver.find_element_by_id('testColor').get_attribute('value'):
        print('ok')
    else:
        print('nem ok')
time.sleep(3)
start_stop()
driver.close()
