from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    # Oldal betöltése
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
    time.sleep(3)

    # A pénzfeldobás gomb kinyerése:
    submit_btn = driver.find_element_by_id('submit')

    # 100 * kattintunk:
    for i in range(100):
        submit_btn.click()

    # Az eledmények listába gyűjtése:
    results_list = driver.find_elements_by_xpath('//ul/li')
    # Annak ellenőrzése, hogy megvan-e a 100 eredmény:
    assert len(results_list) == 100

    # Az eredmények szövegének kinyerése:
    results_list_text = []
    for i in results_list:
        results_list_text.append(i.text)

    # Megszámoljuk, hány 'fej' eredmény született:
    heads = 0
    for i in results_list_text:
        if i == 'fej':
            heads += 1
        else:
            continue

    print(heads)

    # A fejek számának legalább 30-nak kell lennie:
    assert heads >= 30

finally:
    driver.close()
