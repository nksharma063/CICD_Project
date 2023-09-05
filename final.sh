#!/bin/bash

# Function to run a Python script and check its success
run_python_script() {
    python "$1"
    if [ $? -eq 0 ]; then
        echo "Script $1 succeeded."
    else
        echo "Script $1 failed."
        exit 1
    fi
}

# Run Python scripts one by one
run_python_script "auto.py"

# If all Python scripts succeed, run deploy.sh
sudo chmod +x deploy.sh 
./deploy.sh