# Asegúrate de tener estas importaciones al inicio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# --- Dentro de la función que hace scraping ---
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Modo sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 1. Ubicación donde instalaste Chrome en render-build.sh
chrome_path = "/opt/render/project/.render/chrome/chrome-linux64/chrome"
chrome_options.binary_location = chrome_path

# 2. Ubicación donde instalaste ChromeDriver
chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver-linux64/chromedriver"

# 3. Inicializar el driver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
