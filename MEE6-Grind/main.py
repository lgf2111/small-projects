from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from itertools import count

driver = webdriver.Edge(r"C:\Users\lgf2111\Documents\edgedriver_win64\msedgedriver.exe")
driver.get("https://discord.com/app")
input('hit enter here after logging in and being in text channel')
for i in count():
    elem = driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div[2]/div')
    elem.send_keys("https://tenor.com/view/yoru-valorant-gaming-gif-21497100")
    elem.send_keys(Keys.ENTER)
    print(f"{i+1} word")
    for j in range(60):
        print(f"{j+1}s")
        sleep(1)
