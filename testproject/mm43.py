from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
    time.sleep(2)

    # Email mező és 'Submit Now!' gomb kinyerése:
    input_email = driver.find_element_by_id('email')
    submit_btn = driver.find_element_by_id('submit')

    # Függvény a mezők törlésére, kitöltésére és beküldésére:
    def fill_and_send_form(email):
        input_email.clear()
        input_email.send_keys(email)
        submit_btn.click()
        time.sleep(2)


    # Helyes kitöltés esete:
    fill_and_send_form('teszt@elek.hu')
    error_message = driver.find_elements_by_class_name('validation-error')
    assert error_message == []

    # Helytelen kitöltés:
    fill_and_send_form('teszt@')
    error_message = driver.find_element_by_class_name('validation-error')
    assert error_message.text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'

    # Üres mezők:
    fill_and_send_form('')
    error_message = driver.find_element_by_class_name('validation-error')
    assert error_message.text == 'Kérjük, töltse ki ezt a mezőt.'

finally:
    driver.close()
