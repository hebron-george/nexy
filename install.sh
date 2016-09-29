#!/bin/bash

# run after a git clone to configure the venv from the root of the clone dir

APP_DIR=/usr/share/nexy
APP=nexy

echo "Copying files to app directory ${APP_DIR}"
mkdir -p ${APP_DIR}

cp -u requirements.txt ${APP_DIR}

# Create virtualenv
cd ${APP_DIR}
command -v virtualenv >/dev/null || 2>&1 || { echo >&2 "virtualenv not found"; exit 1; }
command -v python2.7 >/dev/null || 2>&1 || { echo >&2 "python2.7 not found"; exit 1; }
command -v pip2.7 >/dev/null || 2>&1 || { echo >&2 "pip not found"; exit 1; }

virtualenv -p $(command -v python2.7) venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

