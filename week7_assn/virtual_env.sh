#!/bin/bash

if [ -d "env" ]; then
    echo "env folder exists. Installing using pip"
else
    echo "Creating env and installing using pip"
    python -m venv env
fi

# Activate the virtual environment
source env/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip

pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
