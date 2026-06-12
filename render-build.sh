#!/usr/bin/env bash
set -o errexit

STORAGE_DIR=/opt/render/project/.render
CHROME_VERSION=131.0.6778.264
CHROMEDRIVER_VERSION=131.0.6778.264

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome v$CHROME_VERSION"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ "https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chrome-linux64.zip"
  unzip chrome-linux64.zip
  rm chrome-linux64.zip
  cd $HOME/project/src
else
  echo "...Using Chrome from cache"
fi

if [[ ! -d $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading ChromeDriver v$CHROMEDRIVER_VERSION"
  mkdir -p $STORAGE_DIR/chromedriver
  cd $STORAGE_DIR/chromedriver
  wget -P ./ "https://storage.googleapis.com/chrome-for-testing-public/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip"
  unzip chromedriver-linux64.zip
  rm chromedriver-linux64.zip
  cd $HOME/project/src
else
  echo "...Using ChromeDriver from cache"
fi

# No necesitas instalar dependencias aquí si ya lo haces en el Build Command de Render
