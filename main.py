from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def get_driver():
    # Rutas donde se instalan Chrome y ChromeDriver durante runtime
    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
    chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver"
    
    # Si no existen, intentar con las rutas alternativas
    if not os.path.exists(chrome_path):
        chrome_path = "/opt/render/project/.render/chrome/chrome"
    if not os.path.exists(chromedriver_path):
        chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver"
    
    # Verificar que los archivos existen
    if not os.path.exists(chrome_path):
        raise Exception(f"Chrome not found at {chrome_path}")
    if not os.path.exists(chromedriver_path):
        raise Exception(f"ChromeDriver not found at {chromedriver_path}")
    
    print(f"✅ Using Chrome: {chrome_path}")
    print(f"✅ Using ChromeDriver: {chromedriver_path}")
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.binary_location = chrome_path
    
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=chrome_options)

# Tu código existente, pero usando get_driver() cuando necesites Selenium
