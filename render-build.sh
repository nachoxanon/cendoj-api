#!/usr/bin/env bash
set -o errexit

# Solo instalamos dependencias de Python aquí
pip install -r requirements.txt

echo "Build completed successfully"
