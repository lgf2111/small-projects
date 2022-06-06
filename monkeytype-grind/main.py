from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pyautogui as pag
from dotenv import load_dotenv
from os import environ
from time import time

pag.PAUSE = .05
load_dotenv()

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("http://www.monkeytype.com/login")
accept_all_btn = driver.find_element(By.XPATH, "/html/body/div[10]/div[2]/div[2]/div[2]/div[1]")
accept_all_btn.click()
email_tbx = driver.find_element(By.XPATH, "/html/body/div[38]/div/div[2]/div[5]/div[3]/form/input[1]")
password_tbx = driver.find_element(By.XPATH, "/html/body/div[38]/div/div[2]/div[5]/div[3]/form/input[2]")
sign_in_btn = driver.find_element(By.XPATH, "/html/body/div[38]/div/div[2]/div[5]/div[3]/form/div[2]")
email_tbx.send_keys(environ['email'])
password_tbx.send_keys(environ['password'])
sign_in_btn.click()
play_btn = driver.find_element(By.XPATH, "/html/body/div[38]/div/div[1]/div[2]/a[1]/div/i")
play_btn.click()
input()
typebox_pos = pag.position()
start_time = time()
while time()-start_time < 17:
    words_txt = driver.find_element(By.ID, "words").text.replace("\n"," ")
    pag.click(typebox_pos)
    for c in words_txt:
        pag.press(c)
        print(time()-start_time)
        if time()-start_time >= 17: break

# driver.close()