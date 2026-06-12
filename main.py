# Importa las nuevas librerías al inicio del archivo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ... dentro de la función que realiza el scraping, reemplaza la línea que crea el driver ...

# Configuración para que Chrome funcione en el servidor de Render
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Modo invisible (necesario en servidores)
chrome_options.add_argument("--no-sandbox")    # Recomendado para entornos Linux
chrome_options.add_argument("--disable-dev-shm-usage") # Para evitar problemas de memoria

# ¡Aquí está la magia! ChromeDriverManager se encarga de todo
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
