from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# Rutas donde Render instala Chrome y ChromeDriver
chrome_path = "/opt/render/project/.render/chrome/chrome-linux64/chrome"
chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver-linux64/chromedriver"

# Verificar si los archivos existen antes de continuar
if not os.path.exists(chrome_path):
    print(f"⚠️ Chrome not found at {chrome_path}")
    # Intentar buscar alternativas
    possible_paths = [
        "/opt/render/project/.render/chrome/chrome-linux64/chrome",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            chrome_path = path
            print(f"✅ Found Chrome at {chrome_path}")
            break

if not os.path.exists(chromedriver_path):
    print(f"⚠️ ChromeDriver not found at {chromedriver_path}")
    # Buscar alternativa
    for path in ["/usr/local/bin/chromedriver", "/usr/bin/chromedriver"]:
        if os.path.exists(path):
            chromedriver_path = path
            print(f"✅ Found ChromeDriver at {chromedriver_path}")
            break

# Configurar Chrome para modo headless
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.binary_location = chrome_path

# Inicializar driver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

print("✅ Chrome initialized successfully")
