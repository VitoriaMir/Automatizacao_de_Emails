# Automatização de Envio de E-mail no Gmail usando Selenium

Este script automatiza o processo de login no Gmail, criação e envio de um novo e-mail.

## Pré-requisitos

- [Python instalado](https://www.python.org/)
- [Selenium WebDriver instalado](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

## Instruções

1. Preencha as variáveis 'email', 'senha', 'para', 'assunto' e 'texto' com suas informações.
2. Certifique-se de ter o WebDriver apropriado instalado e configurado.
3. Execute o script.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (certifique-se de ter o WebDriver adequado instalado)
driver = webdriver.Chrome()

# Acesse a página de login do Gmail
driver.get("https://mail.google.com")
time.sleep(2)

# Preencha o campo de e-mail
email = "seu_email@gmail.com"
driver.find_element(By.ID, "identifierId").send_keys(email)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(2)

# Preencha o campo de senha
senha = "sua_senha"
driver.find_element(By.NAME, "password").send_keys(senha)
driver.find_element(By.ID, "passwordNext").click()
time.sleep(2)

# Crie um novo e-mail
driver.find_element(By.CLASS_NAME, "z0").click()
time.sleep(2)

# Preencha o campo "Para"
para = ''
driver.find_element(By.CLASS_NAME, "agP aFw").send_keys(para)
time.sleep(2)

# Preencha o campo "Assunto"
assunto = ''
driver.find_element(By.CLASS_NAME, "aoT").send_keys(assunto)
time.sleep(2)

# Preencha o corpo do e-mail
texto = ''
driver.find_element(By.CLASS_NAME, "Am Al editable LW-avf tS-tW").send_keys(texto)
time.sleep(2)

# Envie o e-mail
driver.find_element(By.CLASS_NAME, "T-I J-J5-Ji aoO v7 T-I-atl L3").click()
time.sleep(2)

# Encerre o WebDriver
driver.quit()
```

Certifique-se de que você tenha o WebDriver apropriado instalado (por exemplo, o ChromeDriver para o navegador Chrome) e que as variáveis de e-mail, senha, para, assunto e texto estejam preenchidas com suas informações antes de executar o script.
