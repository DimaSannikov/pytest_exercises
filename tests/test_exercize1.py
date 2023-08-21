import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

browser = webdriver.Chrome()
browser.maximize_window()
timer = 0.5
url = "http://google.com"


@pytest.fixture()
def status():
    req = requests.get(url)
    print(f"Status code is {req.status_code}")


def test_start(status):
    browser.get(url)
    
    req = requests.get(url)
    assert req.status_code == 200, "Status code is not 200"

def test_input():
    browser.find_element(By.ID, "APjFqb").send_keys("калькулятор")
    sleep(timer)

def test_send():
    browser.find_elements(By.XPATH, "//input[@name='btnK']")[0].click()
    sleep(timer)

def test_expression():
    expression = "4×9−37+1"
    calc = browser.find_elements(By.CLASS_NAME, "MjjYud")[0].find_elements(By.CLASS_NAME, "ElumCf")[-1]
    for i in expression:
        button = calc.find_elements(By.CLASS_NAME, "PaQdxb")
        for j in button:
            if i == j.text:
                j.click()
            # print(j.text, type(j.text))
    calc.find_element(By.XPATH, "//div[@jsname='Pt8tGc']").click()
    sleep(timer)

def test_result():
    result_1 = browser.find_element(By.XPATH, "//span[@jsname='ubtiRe']").text
    result_2 = browser.find_element(By.XPATH, "//span[@jsname='VssY5c']").text
    print(f"{result_1} {result_2}")
    assert result_1 == "4 × 9 - 37 + 1 =" and  result_2 == "0", "Positive result"

# test_start()
# test_input()
# test_send()
# test_expression()
# test_result()