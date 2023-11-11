#!/bin/bash

VENV_NAME = env
REQUIREMENTS_FILE = requirements.txt

python -m venv $VENV_NAME

source $VENV_NAME/Scripts/Activate.ps1

if [ -f $REQUIREMENTS_FILE ]; then
    pip install -r $REQUIREMENTS_FILE
fi

echo $VENV_NAME > .venv