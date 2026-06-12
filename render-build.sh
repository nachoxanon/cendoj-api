#!/usr/bin/env bash
set -o errexit

STORAGE_DIR=/opt/render/project/.render
CHROME_VERSION=131.0.6778.264

# Instalar Chrome
if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome v$CHROME_VERSION"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ "https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chrome-linux64.zip"
  unzip -q chrome-linux64.zip
  rm chrome-linux64.zip
  cd $HOME/project/src
  
  # Verificar que Chrome existe
  if [[ -f "$STORAGE_DIR/chrome/chrome-linux64/chrome" ]]; then
    echo "✅ Chrome installed successfully at $STORAGE_DIR/chrome/chrome-linux64/chrome"
  else
    echo "❌ Chrome installation failed - binary not found"
    exit 1
  fi
else
  echo "...Using Chrome from cache"
fi

# Instalar ChromeDriver con la misma versión
if [[ ! -d $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading ChromeDriver v$CHROME_VERSION"
  mkdir -p $STORAGE_DIR/chromedriver
  cd $STORAGE_DIR/chromedriver
  wget -P ./ "https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip"
  unzip -q chromedriver-linux64.zip
  rm chromedriver-linux64.zip
  cd $HOME/project/src
  
  # Verificar que ChromeDriver existe
  if [[ -f "$STORAGE_DIR/chromedriver/chromedriver-linux64/chromedriver" ]]; then
    echo "✅ ChromeDriver installed successfully at $STORAGE_DIR/chromedriver/chromedriver-linux64/chromedriver"
  else
    echo "❌ ChromeDriver installation failed - binary not found"
    exit 1
  fi
else
  echo "...Using ChromeDriver from cache"
fi

echo "Build script completed successfully"
