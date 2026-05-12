import time
import os
import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

load_dotenv()
MATRICULA = os.getenv("SUAP_MATRICULA")
SENHA = os.getenv("SUAP_SENHA")

edge_options = Options()
edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--window-size=1920,1080")

meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

hoje = datetime.datetime.now()
amanha = hoje + datetime.timedelta(days=1)

datas_alvo = {
    f"{hoje.day} de {meses[hoje.month]} de {hoje.year}",
    f"{hoje.day:02d} de {meses[hoje.month]} de {hoje.year}",
    f"{amanha.day} de {meses[amanha.month]} de {amanha.year}",
    f"{amanha.day:02d} de {meses[amanha.month]} de {amanha.year}",
}

print(f"🤖 Bot Sniper iniciado de forma invisível...")

driver = webdriver.Edge(options=edge_options)

try:
    driver.get("https://suap.ifpi.edu.br/accounts/login/?next=/")
    driver.find_element(By.ID, "id_username").send_keys(MATRICULA)
    driver.find_element(By.ID, "id_password").send_keys(SENHA)
    driver.find_element(By.CSS_SELECTOR, "input.btn.success").click()
    time.sleep(3)

    driver.get("https://suap.ifpi.edu.br/ae/refeicoes-do-dia/")
    time.sleep(2)

    todos_cartoes = driver.find_elements(By.XPATH, "//div[contains(@class, 'card')]")
    urls_para_reservar = []

    for i, cartao in enumerate(todos_cartoes):
        try:
            h5 = cartao.find_element(By.TAG_NAME, "h5").text.strip()
        except:
            continue

        if h5 != "JANTAR":
            continue

        dts = cartao.find_elements(By.TAG_NAME, "dt")
        dds = cartao.find_elements(By.TAG_NAME, "dd")

        for j in range(len(dts)):
            if "Data da Refeição" in dts[j].text:
                texto_data = dds[j].text.strip()
                if any(data in texto_data for data in datas_alvo):
                    try:
                        botao = cartao.find_element(By.XPATH, ".//a[contains(@class, 'success')]")
                        url = botao.get_attribute("href")
                        urls_para_reservar.append((texto_data, url))
                    except:
                        pass
                break

    if urls_para_reservar:
        for data_refeicao, url in urls_para_reservar:
            driver.get(url)
            time.sleep(3)
    else:
        pass

except Exception as e:
    pass

finally:
    driver.quit()