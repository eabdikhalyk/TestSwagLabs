from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(r"C:\Users\user\PycharmProjects\pythonProject\web_driver\chromedriver.exe")

def test_start():
    browser.get("https://www.saucedemo.com/")

def test_auth():
    user_name = "standard_user"
    password = "secret_sauce"
    title_name = "Products"

    user_name_field = browser.find_element(By.ID,"user-name")
    user_name_field.click()
    user_name_field.send_keys(user_name)

    password_field = browser.find_element(By.ID,"password")
    password_field.click()
    password_field.send_keys(password)

    login = browser.find_element(By.ID,"login-button")
    login.click()

    title = browser.find_element(By.CLASS_NAME,"title")

    assert title.text.lower() == title_name.lower()



