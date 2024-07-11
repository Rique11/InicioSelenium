from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time



# Configurações de opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")  # Descomente para rodar sem interface gráfica


def instanciaChromeDriver():
    
    driver_manager = ChromeDriverManager()
    driver_path = driver_manager.install()
    service = Service(driver_path)
    return service
def ler_arquivo_leilao():
    with open('beeMovie.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas: 
            enviaMensagem(linha.split('\n'))

            
    
    
def enviaMensagem(linha):
        # Enviar mensagens do leilão
            # Enviar mensagem
            barra_mensagem = navegador.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')
            barra_mensagem.click()
            barra_mensagem.send_keys(linha)           
            barra_mensagem.send_keys(Keys.RETURN)
            # Esperar um pouco antes de enviar a próxima mensagem
            time.sleep(5)
    
    
# Instanciar o ChromeDriverManager
service = instanciaChromeDriver() 
# Inicializar o navegador com as opções configuradas
navegador = webdriver.Chrome(service=service, options=chrome_options)
#leArquivo

# Abrir o WhatsApp Web
navegador.get("https://web.whatsapp.com")
print("Navegador iniciado com sucesso!")

input("De Enter quando whatsapp Web estiver aberto, logado e carregado: ")  #TESTE
print("cabo o tempo")  #TESTE

# Nome do contato para quem você enviou a mensagem
contato_nome = 'michel'
chat_xpath = f'//span[@title="{contato_nome}"]'
chat = WebDriverWait(navegador, 30).until(EC.presence_of_element_located((By.XPATH, chat_xpath)))
chat.click()

ler_arquivo_leilao()
