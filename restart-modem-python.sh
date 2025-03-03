#!/bin/bash

# apt update
# apt install -y python3-pip

# python3 -m venv venv
source /usr/local/bin/restart-modem/venv/bin/activate

# python3 -m pip install -r requirements.txt
python3 /usr/local/bin/restart-modem/src/reboot.py