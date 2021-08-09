from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
    time.sleep(3)

    # Oldalon található mezők és gombok kinyerése:
    input_a = driver.find_element_by_id('a')
    input_b = driver.find_element_by_id('b')
    submit_btn = driver.find_element_by_id('submit')


    # Függvény az adatok törlésére , kitöltésére és beküldésére:
    def field_filler_submit(a, b):
        input_a.clear()
        input_b.clear()
        input_a.send_keys(a)
        input_b.send_keys(b)
        submit_btn.click()
        time.sleep(1)


    # Helyes kitöltés esete:
    field_filler_submit('99', '12')
    result = driver.find_element_by_id('result')

    assert result.text == '222'

    # Nem számokkal történő kitöltés:
    field_filler_submit('kiskutya', '12')
    result = driver.find_element_by_id('result')

    assert result.text == 'NaN'

    # Üres kitöltés:
    field_filler_submit('', '')
    result = driver.find_element_by_id('result')

    assert result.text == 'NaN'

finally:
    driver.close()
