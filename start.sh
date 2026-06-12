#!/usr/bin/env bash
set -o errexit

# Crear directorios para Chrome si no existen
mkdir -p /opt/render/project/.render/chrome
mkdir -p /opt/render/project/.render/chromedriver

# Instalar Chrome si no está presente
if [[ ! -f /opt/render/project/.render/chrome/chrome ]]; then
    echo "📦 Installing Chrome..."
    cd /opt/render/project/.render/chrome
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -x google-chrome-stable_current_amd64.deb .
    rm google-chrome-stable_current_amd64.deb
    # Crear un enlace simbólico para tener una ruta fija
    ln -sf /opt/render/project/.render/chrome/opt/google/chrome/chrome /opt/render/project/.render/chrome/chrome
    echo "✅ Chrome installed"
else
    echo "✅ Chrome already installed"
fi

# Instalar ChromeDriver si no está presente
if [[ ! -f /opt/render/project/.render/chromedriver/chromedriver ]]; then
    echo "📦 Installing ChromeDriver..."
    cd /opt/render/project/.render/chromedriver
    CHROME_VERSION=$(/opt/render/project/.render/chrome/chrome --version | awk '{print $3}')
    echo "Chrome version: $CHROME_VERSION"
    # Extraer la versión mayor para el ChromeDriver
    CHROME_MAJOR_VERSION=$(echo $CHROME_VERSION | cut -d '.' -f 1)
    wget -q "https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip"
    unzip -q chromedriver-linux64.zip
    rm chromedriver-linux64.zip
    mv chromedriver-linux64/chromedriver .
    echo "✅ ChromeDriver installed"
else
    echo "✅ ChromeDriver already installed"
fi

# Exportar variables de entorno para que Selenium encuentre Chrome
export PATH="/opt/render/project/.render/chrome/opt/google/chrome:$PATH"
export PATH="/opt/render/project/.render/chromedriver:$PATH"

# Iniciar la aplicación con gunicorn
echo "🚀 Starting application..."
gunicorn main:app
