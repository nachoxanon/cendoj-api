from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ruta fija de Chrome (coincide con render-build.sh)
chrome_options.binary_location = "/opt/render/project/.render/chrome/chrome-linux64/chrome"

# Ruta fija de ChromeDriver
chromedriver_path = "/opt/render/project/.render/chromedriver/chromedriver-linux64/chromedriver"

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
