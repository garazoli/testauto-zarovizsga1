from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
    time.sleep(2)

    # Adatok és Kalkuláció gomb kinyerése:
    num_1 = driver.find_element_by_id('num1')
    num_2 = driver.find_element_by_id('num2')
    op = driver.find_element_by_id('op')
    calc_button = driver.find_element_by_id('submit')

    # Kalkuláció gombra kattintás:
    calc_button.click()
    time.sleep(1)

    # Az oldal által számolt eredmény kinyerése:
    result = driver.find_element_by_id('result')

    # A begyűjtött operandusok és operátor által meghatározott művelet elvégzése:
    if op.text == '+':
        py_result = int(num_1.text) + int(num_2.text)
    elif op.text == '-':
        py_result = int(num_1.text) - int(num_2.text)
    else:
        py_result = int(num_1.text) * int(num_2.text)
    # A forrásban ellenőriztem, hogy ezt a három műveletet kezeli az oldal (+,-,*)

    # A begyűjtött eredmény összevetése a számolt eredménnyel:
    assert int(result.text) == py_result

finally:
    driver.close()
