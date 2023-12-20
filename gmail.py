from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://mail.google.com")
time.sleep(2)

email = "seu_email@gmail.com"
senha = "sua_senha"
driver.find_element(By.ID, "identifierId").send_keys(email)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys(senha)

driver.find_element(By.ID, "passwordNext").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, "z0").click()
time.sleep(2)

para = ''
driver.find_element(By.CLASS_NAME, "agP aFw").send_keys(para)
time.sleep(2)

assunto = ''
driver.find_element(By.CLASS_NAME, "aoT").send_keys(assunto)
time.sleep(2)

texto = ''
driver.find_element(By.CLASS_NAME, "Am Al editable LW-avf tS-tW").send_keys(texto)
time.sleep(2)

driver.find_element(By.CLASS_NAME, "T-I J-J5-Ji aoO v7 T-I-atl L3").click()
time.sleep(2)

driver.quit()
