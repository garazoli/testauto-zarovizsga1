from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
    time.sleep(2)

    # Beviteli mező, Ellenőrzés gomb és városok kinyerése:
    missing_city_field = driver.find_element_by_id('missingCity')
    submit_btn = driver.find_element_by_id('submit')

    cities = driver.find_element_by_id('cites')
    cities_rep = cities.text.replace('"', '')  # Az " jeleket kivettem a stringből
    cities_split_list = cities_rep.split(', ')  # A ', ' karakterekkel elválasztva listába raktam

    # Az oldal által fesorolt városok, amik közül hiányzik egy a fentiekből:
    cities_second_list = []
    second_list = driver.find_elements_by_xpath('//ul/li')
    for i in second_list:
        cities_second_list.append(i.text)

    # A ciklus, ami megtalálja, hogy melyik város nincs a listában, és beküldi a megoldást
    for i in cities_split_list:
        if i not in cities_second_list:
            missing_city_field.send_keys(i)
            submit_btn.click()
            time.sleep(1)
        else:
            continue

    result = driver.find_element_by_id('result')

    assert result.text == 'Eltaláltad.'

finally:
    driver.close()
